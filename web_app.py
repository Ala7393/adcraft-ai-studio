import streamlit as st
from google import genai
import replicate
import os
import time

# =======================================================
# 1. جلب المفاتيح الصافية والآمنة من خزنة السيرفر السحابي
# =======================================================
MY_GEMINI_KEY = st.secrets["GEMINI_API_KEY"]
MY_REPLICATE_KEY = st.secrets["REPLICATE_API_TOKEN"]

os.environ["REPLICATE_API_TOKEN"] = MY_REPLICATE_KEY
os.environ["GEMINI_API_KEY"] = MY_GEMINI_KEY

client = genai.Client(api_key=MY_GEMINI_KEY)
rep_client = replicate.Client(api_token=MY_REPLICATE_KEY)

# ==========================================
# 2. إعدادات واجهة المستخدم المتقدمة (SaaS Dashboard)
# ==========================================
st.set_page_config(
    page_title="AdCraft AI Studio | المنصة المتكاملة", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم بصري متقدم ومريح للعين باستخدام CSS متطور
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    h1, h2, h3, p, span, button { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif !important; }
    div[data-testid="stVerticalBlock"] > div {
        background-color: #ffffff; padding: 26px; border-radius: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        margin-bottom: 24px; border: 1px solid #f1f5f9;
    }
    .stButton>button {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: white !important; border-radius: 12px !important; padding: 16px 32px !important;
        font-weight: 700 !important; font-size: 18px !important; width: 100% !important; border: none !important;
        box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.2) !important; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .stButton>button:hover {
        transform: translateY(-3px); box-shadow: 0 20px 25px -5px rgba(16, 185, 129, 0.4) !important;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        border-radius: 10px !important; border: 1px solid #e2e8f0 !important; padding: 6px 12px !important;
    }
    .stFileUploader {
        border: 2px dashed #10B981 !important; border-radius: 14px !important; background-color: #fcfdfd !important;
    }
    .stProgress > div > div > div > div { background-color: #10B981 !important; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. تصميم الشريط الجانبي (Sidebar) الاحترافي
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #0F172A;'>💼 لوحة التحكم</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 👤 نوع الحساب")
    st.info("💎 الباقة الاحترافية الفاخرة (Premium)")
    st.markdown("### 📊 استهلاك الرصيد")
    st.write("الصور المتبقية: **48 / 50**")
    st.progress(0.96)
    st.markdown("---")
    st.markdown("### 💳 باقات الأسعار المقترحة للتاجر")
    with st.expander("👁️ عرض خطط الاشتراك المتاحة"):
        st.write("• **الباقة الفضية**: 10 إعلانات/شهر بـ **$9.99**")
        st.write("• **الباقة الذهبية**: 50 إعلان/شهر بـ **$29.99**")
        st.write("• **الباقة اللامحدودة**: إعلانات غير محدودة بـ **$79.99**")
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 12px;'>AdCraft AI v2.5 © 2026</p>", unsafe_allow_html=True)

# ==========================================
# 4. واجهة التطبيق الرئيسية (Main Layout)
# ==========================================
st.markdown("""
    <div style='text-align: center; padding: 10px 0px;'>
        <h1 style='color: #0F172A; font-size: 2.8rem; margin-bottom: 8px;'>🚀 استوديو AdCraft AI المحترف</h1>
        <p style='color: #475569; font-size: 1.2rem; max-width: 750px; margin: 0 auto;'>
            المنصة السحابية الأولى للتجار؛ ارفع صورة منتجك الحقيقي ودع الخوارزميات تصنع لك حملة تسويقية سينمائية متكاملة لزيادة مبيعاتك فوراً.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col_input, col_output = st.columns([1, 1.2], gap="large")

with col_input:
    with st.container():
        st.markdown("<h3 style='color: #059669; margin-top:0;'>📸 1. ارفع صورة منتجك الحقيقي</h3>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("قم بسحب وإفلات صورة منتجك هنا (JPG, PNG):", type=["png", "jpg", "jpeg"])
        if uploaded_file is not None:
            st.markdown("---")
            st.image(uploaded_file, caption="📸 صورة منتجك الأصلية المرفوعة", use_container_width=True)

    with st.container():
        st.markdown("<h3 style='color: #059669; margin-top:0;'>🎯 2. هندسة الهوية الإعلانية</h3>", unsafe_allow_html=True)
        shop_name = st.text_input("🏪 اسم متجرك أو علامتك التجارية:", placeholder="مثال: لورا للأزياء")
        product_name = st.text_input("📦 ما هو هذا المنتج؟ (الوصف):", placeholder="مثال: عطر ملكي فاخر برائحة العود")
        
        col_sub1, col_sub2 = st.columns(2)
        with col_sub1:
            platform = st.selectbox("📱 منصة النشر الرئيسية للحملة:", ["تيك توك (TikTok)", "انستغرام (Instagram)"])
        with col_sub2:
            dialect = st.selectbox("🗣️ اللهجة التسويقية المطلوبة:", ["عامية سعودية الخليجية", "عامية مصرية خفيفة"])
            
    with st.container():
        st.markdown("<h3 style='color: #059669; margin-top:0;'>🎵 3. الأجواء الموسيقية للإعلان</h3>", unsafe_allow_html=True)
        music_style = st.selectbox("🎼 اختر نوع ومود الموسيقى الخلفية للإعلان:", [
            "Energetic Modern Hip-Hop Beats",
            "Luxury Cinematic Corporate Sound",
            "Arabic Tech Beats with modern rhythms"
        ])
        st.write("")
        submit_btn = st.button("✨ ⚡ ابدأ إنتاج الحملة التسويقية المتكاملة")

with col_output:
    with st.container():
        st.markdown("<h3 style='color: #0F172A; margin-top:0;'>📋 استوديو الحملة التسويقية الجاهزة</h3>", unsafe_allow_html=True)
        st.write("جميع مخرجات حملتك الاحترافية المجهزة للبيع ستظهر في بطاقات منفصلة بالأسفل.")
        st.write("---")
        
        if submit_btn:
            if shop_name and product_name and uploaded_file is not None:
                
                # --- المرحلة 1: النص التسويقي المقنع (Gemini) ---
                with st.spinner("✍️ جاري صياغة النص الإعلاني الخاطف بأسلوب بشرّي..."):
                    system_prompt = f"أنت خبير تسويق رقمي محترف. اكتب نص إعلاني لـ {platform} باسم {shop_name} عن منتج {product_name} بلهجة {dialect}."
                    try:
                        response = client.models.generate_content(model='gemini-2.5-flash', contents=system_prompt)
                        st.markdown("<div style='background-color: #ecfdf5; padding: 12px; border-radius: 8px; color: #065f46; font-weight: bold;'>📝 أولاً: نص الإعلان الجاهز للنشر:</div>", unsafe_allow_html=True)
                        st.text_area("📋 انسخ النص التسويقي من هنا:", value=response.text, height=140)
                    except Exception as e:
                        st.error(f"خطأ في توليد النص: {e}")

                image_url_string = None

                # --- المرحلة 2: استوديو الصور الفاخر (Flux-2 Pro) ---
                st.write("")
                with st.spinner("🖼️ ثانياً: جاري تشغيل ذكاء Flux لإنشاء صورة استوديو احترافية..."):
                    try:
                        output_image = rep_client.run(
                            "black-forest-labs/flux-2-pro",
                            input={
                                "prompt": f"A high-end luxury professional commercial product photography of {product_name} from {shop_name}, placed beautifully on a polished studio table, cinematic lighting, 8k resolution",
                                "resolution": "1 MP",
                                "aspect_ratio": "1:1",
                                "output_format": "webp"
                            }
                        )
                        image_url_string = str(output_image)
                        final_image_bytes = output_image.read()
                        st.markdown("<div style='background-color: #ecfdf5; padding: 12px; border-radius: 8px; color: #065f46; font-weight: bold;'>🖼️ ثانياً: البوستر الإعلاني الاحترافي لمنتجك:</div>", unsafe_allow_html=True)
                        st.image(final_image_bytes, caption="✨ النتيجة الفوتوغرافية السينمائية بذكاء Flux", use_container_width=True)
                        st.download_button(label="📥 تحميل البوستر بجودة عالية", data=final_image_bytes, file_name=f"{shop_name}_product.webp", mime="image/webp")
                    except Exception as e:
                        st.error(f"حدث خطأ أثناء معالجة الصورة في سيرفر ريبليك: {e}")

                # زيادة الفاصل الزمن لتفادي الـ 429
                time.sleep(5.0)

                # --- المرحلة 3: فيديو الإعلان المتحرك (Stable Video Diffusion) ---
                st.write("")
                with st.spinner("🎥 ثالثاً: جاري بث الحياة وتحريك البوستر إلى فيديو إعلاني قصير..."):
                    try:
                        input_for_video = image_url_string if image_url_string else uploaded_file
                        output_video = rep_client.run(
                            "stability-ai/stable-video-diffusion",
                            input={
                                "input_image": input_for_video,
                                "video_length": "14_frames_with_svd_xt"
                            }
                        )
                        video_bytes = output_video.read()
                        st.markdown("<div style='background-color: #ecfdf5; padding: 12px; border-radius: 8px; color: #065f46; font-weight: bold;'>🎥 ثالثاً: فيديو الإعلان المتحرك والسينمائي للمنتج:</div>", unsafe_allow_html=True)
                        st.video(video_bytes)
                        st.download_button(label="📥 تحميل الفيديو الإعلاني (MP4)", data=video_bytes, file_name=f"{shop_name}_ad_video.mp4", mime="video/mp4")
                    except Exception as e:
