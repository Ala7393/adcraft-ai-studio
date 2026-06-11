import streamlit as st
from google import genai
import replicate
import os

# ==========================================
# 1. إعداد جلب مفاتيح الـ API بشكل آمن وصحيح
# ==========================================
MY_GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
MY_REPLICATE_KEY = os.environ.get("REPLICATE_API_TOKEN")

# الربط الصريح والآمن للسيرفر السحابي
client = genai.Client(api_key=MY_GEMINI_KEY)
replicate_client = replicate.Client(api_token=MY_REPLICATE_KEY)

# ==========================================
# 2. إعدادات واجهة المستخدم (التصميم العصري)
# ==========================================
st.set_page_config(
    page_title="AdCraft AI | استوديو التجار الذكي", 
    page_icon="🎬", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    h1, h2, h3 { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; font-weight: 700 !important; }
    div[data-testid="stVerticalBlock"] > div {
        background-color: #ffffff; padding: 24px; border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        color: white !important; border-radius: 10px !important; padding: 14px 28px !important;
        font-weight: 600 !important; font-size: 16px !important; width: 100% !important; border: none !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2); transition: all 0.3s ease !important;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(37, 99, 235, 0.3); }
    .stTextInput>div>div>input, .stSelectbox>div>div>div { border-radius: 8px !important; border: 1px solid #E2E8F0 !important; }
    .stFileUploader { border: 2px dashed #CBD5E1 !important; border-radius: 12px !important; background-color: #F8FAFC !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; padding: 20px 0px;'>
        <h1 style='color: #0F172A; font-size: 2.5rem; margin-bottom: 8px;'>🎬 استوديو AdCraft AI المحترف</h1>
        <p style='color: #64748B; font-size: 1.1rem; max-width: 600px; margin: 0 auto;'>
            حوّل صور منتجاتك العادية إلى حملات إعلانية مرئية ونصية متكاملة تضاعف مبيعاتك بضغطة زر.
        </p>
    </div>
    """, unsafe_allow_html=True)

col_input, col_output = st.columns([1, 1.1], gap="large")

with col_input:
    with st.container():
        st.markdown("<h3 style='color: #1E3A8A; margin-top:0;'>📸 1. معرض صور المنتج</h3>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("قم بسحب وإفلات صورة منتجك هنا (JPG, PNG):", type=["png", "jpg", "jpeg"])
        if uploaded_file is not None:
            st.image(uploaded_file, caption="الصورة الأصلية المرفوعة للمنتج", use_container_width=True)

    with st.container():
        st.markdown("<h3 style='color: #1E3A8A; margin-top:0;'>🎯 2. هندسة الحملة الإعلانية</h3>", unsafe_allow_html=True)
        shop_name = st.text_input("🏪 اسم متجرك أو علامتك التجارية:", placeholder="مثال: لورا للأزياء")
        product_name = st.text_input("📦 ما هو هذا المنتج؟ (الوصف):", placeholder="مثال: فستان سهرة فخم")
        
        col_sub1, col_sub2 = st.columns(2)
        with col_sub1:
            platform = st.selectbox("📱 منصة الإعلان الرئيسية:", ["تيك توك (TikTok)", "انستغرام (Instagram)"])
        with col_sub2:
            dialect = st.selectbox("🗣️ اللهجة الصوتية المستهدفة:", ["عامية سعودية الخليجية", "عامية مصرية خفيفة"])
    
    with st.container():
        st.markdown("<h3 style='color: #1E3A8A; margin-top:0;'>⚡ 3. الخدمات المطلوبة</h3>", unsafe_allow_html=True)
        enhance_bg = st.checkbox("🖼️ توليد صورة استوديو إعلاني احترافي بذكاء Flux", value=True)
        convert_to_video = st.checkbox("🎥 تحويل الصورة لفيديو سينمائي متحرك", value=False)
        st.write("")
        submit_btn = st.button("🚀 ابدأ المعالجة الذكية والإنتاج")

with col_output:
    with st.container():
        st.markdown("<h3 style='color: #0F172A; margin-top:0;'>📋 استوديو المخرجات الاحترافية</h3>", unsafe_allow_html=True)
        st.write("النتائج وحملاتك التسويقية ستظهر هنا فوراً.")
        st.write("---")
        
        if submit_btn:
            if shop_name and product_name and uploaded_file is not None:
                
                # --- المرحلة 1: النص الإعلاني (Gemini) ---
                with st.spinner("✍️ جاري صياغة النص الإعلاني بأسلوب تسويقي..."):
                    system_prompt = f"أنت خبير تسويق محترف. اكتب نص إعلاني لـ {platform} باسم {shop_name} عن منتج {product_name} بلهجة {dialect}."
                    try:
                        response = client.models.generate_content(model='gemini-2.0-flash', contents=system_prompt)
                        st.markdown("<b style='color:#10B981;'>✅ تم صياغة النص الإعلاني بنجاح:</b>", unsafe_allow_html=True)
                        st.text_area("📋 نص الإعلان الجاهز:", value=response.text, height=150)
                    except Exception as e:
                        st.error(f"خطأ في توليد النص: {e}")

                image_url_string = None

                # --- المرحلة 2: توليد الصورة بـ Flux وعرضها ---
                if enhance_bg:
                    st.write("")
                    with st.spinner("🖼️ جاري تشغيل ذكاء Flux لبناء الاستوديو الإعلاني الفاخر..."):
                        try:
                            output_image = replicate_client.run(
                                "black-forest-labs/flux-2-pro",
                                input={
                                    "prompt": f"A high-end luxury professional commercial product photography of {product_name} from {shop_name}, placed beautifully on a polished studio table, cinematic lighting, 8k resolution",
                                    "resolution": "1 MP",
                                    "aspect_ratio": "1:1",
                                    "output_format": "webp"
                                }
                            )
                            # قراءة الرابط كنص مخصص لتمهيده للفيديو بسلام
                            image_url_string = str(output_image)
                            final_image_bytes = output_image.read()
                            
                            st.markdown("<b style='color:#10B981;'>✅ تم توليد التصميم البصري بنجاح:</b>", unsafe_allow_html=True)
                            st.image(final_image_bytes, caption="✨ النتيجة السينمائية الحقيقية بذكاء Flux", use_container_width=True)
                        except Exception as e:
                            st.error(f"حدث خطأ أثناء معالجة الصورة في سيرفر ريبليك: {e}")

                # --- المرحلة 3: تحويل صورة المنتج لفيديو متحرك حقيقي عبر الـ client الموثق الصارم ---
                if convert_to_video:
                    st.write("")
                    with st.spinner("🎥 جاري تحريك المشهد وضبط تأثيرات الكاميرا السينمائية..."):
                        try:
                            # إذا لم تتوفر صورة معدلة نستخدم ملف العميل الأصلي مباشرة بعد قراءة الرابط
                            input_for_video = image_url_string if image_url_string else uploaded_file

                            # تصحيح صارم: تمرير الطلب عبر replicate_client لحل مشكلة الـ 401 للفيديو
                            output_video = replicate_client.run(
                                "stability-ai/stable-video-diffusion:3f2d6c5b9f3b3920db22dee2905cc380e8e4544d6c5b9f3b3920db22dee2905cc380e",
                                input={
                                    "input_image": input_for_video,
                                    "video_length": "14_frames_with_svd_xt"
                                }
                            )
                            st.markdown("<b style='color:#10B981;'>✅ فيديو الإعلان القصير جاهز:</b>", unsafe_allow_html=True)
                            st.video(output_video.read())
                        except Exception as e:
                            st.error(f"حدث خطأ أثناء تحويل صورة منتجك إلى فيديو: {e}")
                            
            elif uploaded_file is None:
                st.warning("⚠️ من فضلك قم برفع صورة المنتج أولاً لبدء المعالجة البصرية.")
            else:
                st.warning("⚠️ يرجى ملء البيانات الأساسية أولاً للبدء.")
