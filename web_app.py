import streamlit as st
from google import genai
import replicate
import os
import time

# ==========================================
# 1. إعداد جلب مفاتيح الـ API بشكل آمن ومخفي
# ==========================================
# هذا التعديل يمنع الحظر الأمني في GitHub ويجلب المفاتيح من الخزنة السرية للسيرفر
MY_GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
MY_REPLICATE_KEY = os.environ.get("REPLICATE_API_TOKEN")

# تفعيل ربط عملاء الذكاء الاصطناعي برمجياً
client = genai.Client(api_key=MY_GEMINI_KEY)
os.environ["REPLICATE_API_TOKEN"] = MY_REPLICATE_KEY

# ==========================================
# 2. إعدادات واجهة المستخدم (تنسيق مخصص وعصري)
# ==========================================
st.set_page_config(
    page_title="AdCraft AI | استوديو التجار الذكي",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تصميم بصري متقدم ومريح للعين باستخدام CSS
st.markdown("""
    <style>
    /* تغيير خلفية الموقع العامة */
    .stApp {
        background-color: #f8fafc;
    }

    /* تحسين شكل النصوص والعناوين بالتنسيق العربي العالمي */
    h1, h2, h3 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-weight: 700 !important;
    }

    /* تصميم بطاقات التحكم المنفصلة */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 20px;
    }

    /* تصميم زر المعالجة الرئيسي الاحترافي مع مؤثر حركي */
    .stButton>button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        color: white !important;
        border-radius: 10px !important;
        padding: 14px 28px !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        width: 100% !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.3);
        background: linear-gradient(135deg, #1D4ED8 0%, #1E40AF 100%);
    }

    /* تحسين حقول الإدخال والقوائم المنسدلة */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        border-radius: 8px !important;
        border: 1px solid #E2E8F0 !important;
    }

    /* تصميم مخصص لصندوق رفع ملفات العميل */
    .stFileUploader {
        border: 2px dashed #CBD5E1 !important;
        border-radius: 12px !important;
        padding: 10px !important;
        background-color: #F8FAFC !important;
    }
    </style>
    """, unsafe_allow_html=True)

# الهيدر والترحيب العلوي بالتاجر
st.markdown("""
    <div style='text-align: center; padding: 20px 0px;'>
        <h1 style='color: #0F172A; font-size: 2.5rem; margin-bottom: 8px;'>🎬 استوديو AdCraft AI المحترف</h1>
        <p style='color: #64748B; font-size: 1.1rem; max-width: 600px; margin: 0 auto;'>
            حوّل صور منتجاتك العادية إلى حملات إعلانية مرئية ونصية متكاملة تضاعف مبيعاتك بضغطة زر.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# تقسيم الشاشة إلى عمودين بنسب متناسقة لعرض الواجهة السحابية
col_input, col_output = st.columns([1, 1.1], gap="large")

with col_input:
    # حاوية مخصصة لرفع صور المنتجات الحقيقية
    with st.container():
        st.markdown("<h3 style='color: #1E3A8A; margin-top:0;'>📸 1. معرض صور المنتج</h3>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("قم بسحب وإفلات صورة منتجك الحقيقي هنا (JPG, PNG):",
                                         type=["png", "jpg", "jpeg"])

        if uploaded_file is not None:
            st.markdown("---")
            st.image(uploaded_file, caption="الصورة الأصلية المرفوعة للمنتج", use_container_width=True)

    # حاوية مدخلات الحملة التسويقية
    with st.container():
        st.markdown("<h3 style='color: #1E3A8A; margin-top:0;'>🎯 2. هندسة الحملة الإعلانية</h3>",
                    unsafe_allow_html=True)
        shop_name = st.text_input("🏪 اسم متجرك أو علامتك التجارية:", placeholder="مثال: لورا للأزياء")
        product_name = st.text_input("📦 ما هو هذا المنتج؟ (الوصف المالي أو الفني):",
                                     placeholder="مثال: فستان سهرة مخملي أسود مطرز")

        col_sub1, col_sub2 = st.columns(2)
        with col_sub1:
            platform = st.selectbox("📱 منصة الإعلان الرئيسية:",
                                    ["تيك توك (TikTok)", "انستغرام (Instagram)", "سناب شات (Snapchat)"])
        with col_sub2:
            dialect = st.selectbox("🗣️ اللهجة الصوتية المستهدفة:",
                                   ["عامية سعودية الخليجية", "عامية مصرية خفيفة", "فصحى مبسطة وجذابة"])

    # حاوية الخيارات والخدمات الذكية المطلوبة
    with st.container():
        st.markdown("<h3 style='color: #1E3A8A; margin-top:0;'>⚡ 3. الخدمات المطلوبة</h3>", unsafe_allow_html=True)
        enhance_bg = st.checkbox("🖼️ عزل المنتج واستبدال الخلفية باستوديو احترافي حقيقي", value=True)
        convert_to_video = st.checkbox("🎥 بث الحياة في الصورة وتحويلها لفيديو سينمائي متحرك", value=False)
        st.write("")
        submit_btn = st.button("🚀 ابدأ المعالجة الذكية والإنتاج")

with col_output:
    with st.container():
        st.markdown("<h3 style='color: #0F172A; margin-top:0;'>📋 استوديو المخرجات الاحترافية</h3>",
                    unsafe_allow_html=True)
        st.write("النتائج وحملاتك التسويقية الحقيقية ستظهر هنا فور الضغط على زر المعالجة.")
        st.write("---")

        if submit_btn:
            if shop_name and product_name and uploaded_file is not None:

                # --- المرحلة 1: النص الإعلاني الذكي من جوجـل (Gemini) ---
                with st.spinner("✍️ جاري صياغة النص الإعلاني بأسلوب تسويقي خطّاف..."):
                    system_prompt = f"""
                    أنت خبير تسويق رقمي محترف ومبدع جداً في كتابة الإعلانات البيعية (Copywriter) في السوق العربي.
                    قم بكتابة نص إعلاني جذاب جداً لمنصة ({platform}) بناءً على المعلومات التالية:
                    - اسم المتجر: {shop_name} - المنتج/الخدمة: {product_name}
                    - اللهجة المطلوبة: {dialect} (اكتب النص كاملاً بهذه اللهجة بدقة وبشكل طبيعي جداً كأنك ابن البلد).
                    الشروط: ابدأ بجملة خطافة لمنع التمرير، ركز على الفوائد، استخدم الإيموجي، واختم بدعوة واضحة لاتخاذ إجراء وقدم 5 هاشتاجات مناسبة.
                    """
                    try:
                        response = client.models.generate_content(model='gemini-2.5-flash', contents=system_prompt)
                        st.markdown("<b style='color:#10B981;'>✅ تم صياغة النص الإعلاني بنجاح:</b>",
                                    unsafe_allow_html=True)
                        st.text_area("📋 نص الإعلان الجاهز للنسخ والاستخدام:", value=response.text, height=180)
                    except Exception as e:
                        st.error(f"خطأ في توليد النص: {e}")

                # متغير وسيط لتمرير الصورة المحسنة واستعمالها في الفيديو
                final_image_url = None

                # --- المرحلة 2: استبدال وتعديل خلفية المنتج (Replicate - SDXL) ---
                if enhance_bg:
                    st.write("")
                    with st.spinner("🖼️ جاري إرسال الصورة للسيرفر لعزل المنتج وتغيير الخلفية تلقائياً..."):
                        try:
                            # الاتصال بنموذج الرسوم واستبدال الخلفية بناءً على اسم المنتج الخاص بالعميل
                            output_image = replicate.run(
                                "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b13c712de7dfea535525255b1aa35c5565e08b",
                                input={
                                    "prompt": f"A high-end professional commercial product photography of {product_name}, placed on a clean luxury studio table, elegant blurred background, cinema lighting, 8k resolution, highly detailed",
                                    "image": uploaded_file,
                                }
                            )
                            final_image_url = output_image
                            st.markdown("<b style='color:#10B981;'>✅ تم إنشاء التصميم البصري الاحترافي الحقيقي:</b>",
                                        unsafe_allow_html=True)
                            st.image(final_image_url, caption="✨ النتيجة: منتجك داخل استوديو إعلاني حقيقي من السيرفر",
                                     use_container_width=True)
                        except Exception as e:
                            st.error(f"حدث خطأ أثناء معالجة الصورة في السيرفر الخارجي: {e}")

                # --- المرحلة 3: تحويل صورة المنتج لفيديو متحرك (Replicate - SVD) ---
                if convert_to_video:
                    st.write("")
                    with st.spinner("🎥 جاري تحريك المشهد وبث الحياة في إضاءة ومحيط المنتج..."):
                        try:
                            # تحديد الصورة المراد تحريكها (الصورة المحسنة بالخلفية الجديدة أو الأصلية المرفوعة)
                            image_to_animate = final_image_url if final_image_url else uploaded_file

                            output_video = replicate.run(
                                "stability-ai/stable-video-diffusion:3f2d6c5b9f3b3920db22dee2905cc380e8e4544d6c5b9f3b3920db22dee2905cc380e",
                                input={
                                    "input_image": image_to_animate,
                                    "video_length": "14_frames_with_svd_xt"
                                }
                            )
                            st.markdown(
                                "<b style='color:#10B981;'>✅ فيديو الإعلان السينمائي القصير جاهز للعرض والتحميل:</b>",
                                unsafe_allow_html=True)
                            st.video(output_video)
                        except Exception as e:
                            st.error(f"حدث خطأ أثناء تحويل صورة منتجك إلى فيديو: {e}")

            elif uploaded_file is None:
                st.warning("⚠️ من فضلك قم برفع صورة المنتج أولاً لبدء المعالجة البصرية.")
            else:
                st.warning("⚠️ يرجى ملء البيانات الأساسية (اسم المتجر ووصف المنتج) أولاً للبدء.")
