import streamlit as st
from google import genai
import replicate
import os

# =======================================================
# 1. جلب المفاتيح الصافية من خزنة السيرفر السحابي المحدثة
# =======================================================
MY_GEMINI_KEY = st.secrets["GEMINI_API_KEY"]
MY_REPLICATE_KEY = st.secrets["REPLICATE_API_TOKEN"]

# حقن المفاتيح في بيئة النظام لتأمين مكتبة ريبليك للفيديو والصوت
os.environ["r8_bseEfbvrNvBvEHnAqMIwBsDo68eFYLm2CA3di"] = MY_REPLICATE_KEY
os.environ["AQ.Ab8RN6INwwjInYGcOuKLzwKEuT5x9G9Y1DzPzL4De_7B-v9QWw"] = MY_GEMINI_KEY

# الربط البرمجي الصارم والآمن للعملاء
client = genai.Client(api_key=MY_GEMINI_KEY)
rep_client = replicate.Client(api_token=MY_REPLICATE_KEY)

# ==========================================
# 2. إعدادات واجهة المستخدم (Premium SaaS Theme)
# ==========================================
st.set_page_config(
    page_title="AdCraft AI Ultimate | استوديو التسويق الشامل", 
    page_icon="🚀", 
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
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: white !important; border-radius: 10px !important; padding: 16px 32px !important;
        font-weight: 700 !important; font-size: 18px !important; width: 100% !important; border: none !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2); transition: all 0.3s ease !important;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(16, 185, 129, 0.3); }
    .stTextInput>div>div>input, .stSelectbox>div>div>div { border-radius: 8px !important; border: 1px solid #E2E8F0 !important; }
    .stFileUploader { border: 2px dashed #10B981 !important; border-radius: 12px !important; background-color: #F8FAFC !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; padding: 20px 0px;'>
        <h1 style='color: #0F172A; font-size: 2.5rem; margin-bottom: 8px;'>🚀 استوديو AdCraft AI للتسويق الشامل</h1>
        <p style='color: #64748B; font-size: 1.1rem; max-width: 700px; margin: 0 auto;'>
            ارفع صورة منتجك فقط.. وشاهد السحر وهو يصنع حملة تسويقية كاملة (إعلان نصي + صورة استوديو + فيديو سينمائي متحرك + موسيقى حماسية خلفية)!
        </p>
    </div>
    """, unsafe_allow_html=True)

col_input, col_output = st.columns([1, 1.1], gap="large")

with col_input:
    with st.container():
        st.markdown("<h3 style='color: #059669; margin-top:0;'>📸 1. ارفع صورة منتجك الحقيقي</h3>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("قم بسحب وإفلات صورة منتجك هنا (JPG, PNG):", type=["png", "jpg", "jpeg"])
        if uploaded_file is not None:
            st.image(uploaded_file, caption="صورة المنتج الأصلية المرفوعة", use_container_width=True)

    with st.container():
        st.markdown("<h3 style='color: #059669; margin-top:0;'>🎯 2. هندسة الهوية الإعلانية</h3>", unsafe_allow_html=True)
        shop_name = st.text_input("🏪 اسم متجرك أو علامتك التجارية:", placeholder="مثال: لورا للأزياء")
        product_name = st.text_input("📦 ما هو هذا المنتج？ (الوصف):", placeholder="مثال: عطر ملكي فاخر برائحة العود")
        
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
        st.markdown("<h3 style='color: #0F172A; margin-top:0;'>📋 معرض الحملة التسويقية الجاهزة</h3>", unsafe_allow_html=True)
        st.write("جميع مخرجات حملتك الاحترافية المجهزة للبيع ستظهر هنا فور الضغط على الزر.")
        st.write("---")
        
        if submit_btn:
            if shop_name and product_name and uploaded_file is not None:
                
                # --- المرحلة 1: النص التسويقي المقنع (Gemini) ---
                with st.spinner("✍️ جاري صياغة النص الإعلاني الخاطف بأسلوب بشري..."):
                    system_prompt = f"أنت خبير تسويق رقمي محترف. اكتب نص إعلاني لـ {platform} باسم {shop_name} عن منتج {product_name} بلهجة {dialect}."
                    try:
                        response = client.models.generate_content(model='gemini-2.5-flash', contents=system_prompt)
                        st.markdown("<b style='color:#10B981;'>📝 أولاً: نص الإعلان الجاهز للنسخ والنشر:</b>", unsafe_allow_html=True)
                        st.text_area("📋 انسخ النص التسويقي من هنا:", value=response.text, height=140)
                    except Exception as e:
                        st.error(f"خطأ في توليد النص: {e}")

                image_url_string = None

                # --- المرحلة 2: استوديو الصور الفاخر (Flux-2 Pro) ---
                st.write("")
                with st.spinner("🖼️ ثانياً: جاري تشغيل ذكاء Flux لإنشاء صورة استوديو احترافية للمنتج..."):
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
                        
                        st.markdown("<b style='color:#10B981;'>🖼️ ثانياً: البوستر الإعلاني الاحترافي لمنتجك:</b>", unsafe_allow_html=True)
                        st.image(final_image_bytes, caption="✨ النتيجة الفوتوغرافية السينمائية بذكاء Flux", use_container_width=True)
                    except Exception as e:
                        st.error(f"حدث خطأ أثناء معالجة الصورة في سيرفر ريبليك: {e}")

                # --- المرحلة 3: فيديو الإعلان المتحرك (Luma Dream Machine) ---
                st.write("")
                with st.spinner("🎥 ثالثاً: جاري بث الحياة وتحريك الصورة إلى فيديو إعلاني قصير..."):
                    try:
                        input_for_video = image_url_string if image_url_string else uploaded_file
                        
                        output_video = rep_client.run(
                            "luma/dream-machine",
                            input={
                                "prompt": f"Cinematic slow motion camera movement around this product {product_name}, professional product advertisement video, commercial concept",
                                "image": input_for_video
                            }
                        )
                        st.markdown("<b style='color:#10B981;'>🎥 ثالثاً: فيديو الإعلان المتحرك والسينمائي للمنتج:</b>", unsafe_allow_html=True)
                        st.video(output_video.read())
                    except Exception as e:
                        st.error(f"حدث خطأ أثناء تحويل صورة منتجك إلى فيديو: {e}")

                # --- المرحلة 4: الموسيقى الإعلانية المتوافقة (Meta MusicGen) ---
                st.write("")
                with st.spinner("🎵 رابعاً: جاري عزف وتوليد تراك موسيقي تجاري خلفي يناسب الحملة..."):
                    try:
                        output_audio = rep_client.run(
                            "meta/musicgen:7a76a825e58c11c5381117437a14be58d0dd99e3e3cf3e3870b92d6e4df46bc2",
                            input={
                                "prompt": f"A commercial advertisement background music, {music_style}, high quality, loops, professional master, electronic beats",
                                "duration": 8
                            }
                        )
                        st.markdown("<b style='color:#10B981;'>🎵 رابعاً: الموسيقى الإعلانية الحصرية المخصصة لمتجرك:</b>", unsafe_allow_html=True)
                        st.audio(output_audio.read())
                    except Exception as e:
                        st.error(f"حدث خطأ أثناء توليد الموسيقى الإعلانية: {e}")
                            
            elif uploaded_file is None:
                st.warning("⚠️ من فضلك قم برفع صورة المنتج أولاً لبدء الإنتاج البصري.")
            else:
                st.warning("⚠️ يرجى ملء البيانات الأساسية أولاً للبدء.")
