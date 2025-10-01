ghostscan/
├─ app/src/main/java/com/ghostscan/MainActivity.kt
├─ native/src/ghostscan.c
├─ native/include/ghostscan.h
├─ CMakeLists.txt

// native/src/ghostscan.c
#include <jni.h>
#include <stdint.h>
#include <stdlib.h>

JNIEXPORT jbyteArray JNICALL
Java_com_ghostscan_MainActivity_nativeScan(JNIEnv* env, jobject thiz,
                                           jbyteArray rgba, jint w, jint h) {
    jbyte* in = (*env)->GetByteArrayElements(env, rgba, NULL);
    int size = w*h;
    jbyteArray outArr = (*env)->NewByteArray(env, size);
    jbyte* out = (*env)->GetByteArrayElements(env, outArr, NULL);

    // Simple grayscale + contrast
    for (int i=0;i<size;i++) {
        int idx = i*4;
        uint8_t r = (uint8_t)in[idx], g = (uint8_t)in[idx+1], b = (uint8_t)in[idx+2];
        int gray = (r*30 + g*59 + b*11)/100;
        gray = (gray < 64) ? 0 : (gray > 192 ? 255 : gray); // crude contrast
        out[i] = (jbyte)gray;
    }

    (*env)->ReleaseByteArrayElements(env, rgba, in, 0);
    (*env)->ReleaseByteArrayElements(env, outArr, out, 0);
    return outArr;
}
class MainActivity : AppCompatActivity() {
    external fun nativeScan(rgba: ByteArray, w: Int, h: Int): ByteArray
    companion object { init { System.loadLibrary("ghostscan") } }

    private lateinit var tts: TextToSpeech
    private val lines = listOf(
        "Bravo, you pressed a button. Genius.",
        "Scan complete. Try not to hurt yourself with all that effort.",
        "Document saved. Don’t spend it all in one place.",
        "Wow, productivity. Alert the media."
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        tts = TextToSpeech(this) { tts.language = Locale("pt", "PT") }
        // UI: one button
        val btn = Button(this).apply {
            text = "Scan"
            setOnClickListener { doScan() }
        }
        setContentView(btn)
    }

    private fun doScan() {
        // Capture RGBA from camera (stubbed here)
        val rgba = ByteArray(100*100*4) // fake frame
        val out = nativeScan(rgba, 100, 100)
        // Save bitmap/PDF (omitted for brevity)
        tts.speak(lines.random(), TextToSpeech.QUEUE_FLUSH, null, "sarcasm")
    }
}
val imageCapture = ImageCapture.Builder().build()
imageCapture.takePicture(ContextCompat.getMainExecutor(this),
    object : ImageCapture.OnImageCapturedCallback() {
        override fun onCaptureSuccess(image: ImageProxy) {
            val buffer = image.planes[0].buffer
            val bytes = ByteArray(buffer.remaining())
            buffer.get(bytes)
            val out = nativeScan(bytes, image.width, image.height)
            // convert to Bitmap, show or save
            image.close()
        }
    })
fun saveAsPdf(bmp: Bitmap, file: File) {
    val pdf = PdfDocument()
    val pageInfo = PdfDocument.PageInfo.Builder(bmp.width, bmp.height, 1).create()
    val page = pdf.startPage(pageInfo)
    page.canvas.drawBitmap(bmp, 0f, 0f, null)
    pdf.finishPage(page)
    file.outputStream().use { pdf.writeTo(it) }
    pdf.close()
}
