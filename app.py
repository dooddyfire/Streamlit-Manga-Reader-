import streamlit as st 
import webbrowser
import uuid
from streamlit_option_menu import option_menu

import streamlit.components.v1 as components


# HTML + CSS for the Navbar
navbar_html = """

    <style>

    @import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
            
                *{
            font-family:Kanit !important;
            }
      /* Navbar container */
      .navbar {
        background-color: #333;
        overflow: hidden;
        border-radius:10px;
        font-family:Kanit;
      }

      /* Navbar links */
      .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
        font-family:Kanit;
      }

      /* Hover effect on links */
      .navbar a:hover {
        background-color: #ddd;
        border-radius:10px;
        color: black;
        font-family:Kanit;
      }

      /* Active link styling */
      .navbar a.active {
        background-color: rgb(255, 51, 51);
        border-radius:10px;
        color: white;
        font-family:Kanit;
      }
    </style>
  

    <div class="navbar">
      <a href="#" class="active">หน้าแรก</a>
      <a href="#998b8830" target="_self">สินค้าของเรา</a>
      
      <a href="https://supapongai.com" target='_blank'>ติดต่อเรา</a>
    </div>

"""

st.markdown(navbar_html,unsafe_allow_html=True)


# HTML + JavaScript for the Slick Slider
slider_html = """

    <!-- Include jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <!-- Include Slick CSS and JS -->
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick-theme.css"/>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>

    <style>
/* Custom styling for the slider */
      .slick-slide {
        text-align: center;
        background: #EEE;
        padding: 20px;
      }

      .slick-prev, .slick-next {
        font-size: 30px;
        color: #000;
      }

      .slick-prev:before, .slick-next:before {
        color: #fff;
      }

      /* Customizing the navigation dots */
      .slick-dots {
        bottom: 0px;  /* Position the dots 5px below the slider */
      }

      .slick-dots li button:before {
        color: #fff;  /* Inactive dots in white */
      }

      /* Active dot color */
      .slick-dots li.slick-active button:before {
        color: yellow;  /* Active dot in yellow */
      }

      /* Make images full cover */
      .slick-slide img {
        width: 100%;
        height: 100%;
        object-fit: cover;  /* Ensures the image covers the entire area */
      }

      /* Set a fixed height for the slider container */
      .slick-slider {
        width: 100%;
        height: 400px;  /* You can adjust the height to fit your needs */
      }
    </style>


    <!-- Slick Slider HTML structure -->
    <div class="slick-slider">
      <div><img src="https://jumpg-assets.tokyo-cdn.com/secure/top_banner/385640.jpg?hash=6U6AugwXkOAdX1grC_G59A&expires=2145884400" style='object-fit:cover' alt="Slide 1"></div>
      <div><img src="https://jumpg-assets.tokyo-cdn.com/secure/top_banner/385640.jpg?hash=6U6AugwXkOAdX1grC_G59A&expires=2145884400" style='object-fit:cover' alt="Slide 2"></div>

    </div>

    <script>
      // Initialize Slick slider
      $(document).ready(function(){
        $('.slick-slider').slick({
          autoplay: true,
          autoplaySpeed: 2000,
          dots: true,  // Enable navigation dots
          arrows: true,  // Enable navigation arrows
          prevArrow: '<button type="button" class="slick-prev">Prev</button>',  // Custom prev arrow
          nextArrow: '<button type="button" class="slick-next">Next</button>'  // Custom next arrow
        });
      });
    </script>
  

"""






with st.container():
    st.markdown(
        """

        <h1 style="text-align: center;font-family:Kanit">
            ร้านหนังสือ SweetieSS ออนไลน์
        </h1>
        """,
        unsafe_allow_html=True,
    )
#page
   # Custom CSS to remove padding
st.markdown(
            """


            <style>
                @import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

            *{
font-family:Kanit !important;            
            }

            .st-emotion-cache-1jicfl2 {
    width: 100%;
    padding: 6rem 1rem 10rem;
    min-width: auto;
    max-width: initial;

    button {
        width: 100% !important;
    }
}
            """,
            unsafe_allow_html=True,
        )
#st.image('https://jumpg-assets.tokyo-cdn.com/secure/top_banner/385640.jpg?hash=6U6AugwXkOAdX1grC_G59A&expires=2145884400')

# Inject the HTML and JavaScript into Streamlit
components.html(slider_html,height=300)

with st.container():
    st.markdown(
        """

        <h2 style="text-align: center;">
            เกี่ยวกับเรา
        </h2>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p style="font-size:18px;">
            ให้บริการจำหน่ายหนังสือ มือ 2  และ มือ 1 ออนไลน์ จัดส่งฟรีทั่วประเทศไทย 
        </p>
        """,
        unsafe_allow_html=True,
    )


st.video('https://www.youtube.com/watch?v=gkbgz_rr4X8')


with st.container():
    st.markdown(
        """
        <h2 style="text-align: center;">
            สินค้าของเรา
        </h2>
        """,
        unsafe_allow_html=True,
    )
# Function to display page 1 content
def display_page1():
    # Create a container for page1
    with st.container():
        # Create six columns for page1
        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)

        # Add content to the first column (col1)
        col1.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 1</h2>", unsafe_allow_html=True)
        col1.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100169/title_thumbnail_portrait_list/315646.jpg?hash=SrZavt9Kq6wVp5wasEwhXA&expires=2145884400')


        col1.write("หนังสือออกใหม่ Date a Live เล่ม 1")
        col1.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())

    # Button with a link
        if col1.button('สั่งซื้อ', key='item1', use_container_width=True,type='secondary'):
            webbrowser.open_new_tab('https://page.line.me/sweetiess')


        # Add content to the second column (col2)
        col2.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 1</h2>", unsafe_allow_html=True)
        col2.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100280/title_thumbnail_portrait_list/317512.jpg?hash=ZcpiFHzWAw1lOJExtQ5U6Q&expires=2145884400')
        col2.write("หนังสือออกใหม่ Date a Live เล่ม 2")

        col2.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        
        if  col2.button('สั่งซื้อ', key='item2', use_container_width=True):
            webbrowser.open_new_tab('https://mangakakalot.com/chapter/kakegurui/chapter_109')



        # Add content to the third column (col3)
        col3.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 1</h2>", unsafe_allow_html=True)
        col3.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100401/title_thumbnail_portrait_list/387680.jpg?hash=KRgd0qeiGw-lmn0J1bmBFQ&expires=2145884400')

        
        col3.write("หนังสือออกใหม่ Date a Live เล่ม 3")

        col3.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        col3.button('สั่งซื้อ', key='item3', use_container_width=True)

        # Add content to the fourth column (col4)
        col4.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 1</h2>", unsafe_allow_html=True)
        col4.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100282/title_thumbnail_portrait_list/319693.jpg?hash=O0h0CmpuRI8GRsMHlGYsKQ&expires=2145884400')
        col4.write("หนังสือออกใหม่ Date a Live เล่ม 4")

        col4.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        col4.button('สั่งซื้อ', key='item4', use_container_width=True)

        # Add content to the fifth column (col5)
        col5.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 1</h2>", unsafe_allow_html=True)
        col5.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100005/title_thumbnail_portrait_list/311848.jpg?hash=h2hrMHKi-kJCkbbpuBQG0Q&expires=2145884400')
        col5.write("หนังสือออกใหม่ Date a Live เล่ม 5")

        col5.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        col5.button('สั่งซื้อ', key='item5', use_container_width=True)

        # Add content to the sixth column (col6)
        col6.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 1</h2>", unsafe_allow_html=True)
        col6.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100183/title_thumbnail_portrait_list/313033.jpg?hash=spgNAUbUV4pzI8FBFx-wTg&expires=2145884400')
        col6.write("หนังสือออกใหม่ Date a Live เล่ม 6")

        col6.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        col6.button('สั่งซื้อ', key='item6', use_container_width=True)

# Function to display page 2 content
def display_page2():
    # Create a container for page2
    with st.container():
        # Create six columns for page2
        col7, col8, col9 = st.columns(3)
        col10, col11, col12 = st.columns(3)

        

        # Add content to the seventh column (col7)
        col7.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 7</h2>", unsafe_allow_html=True)
        col7.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100004/title_thumbnail_portrait_list/311788.jpg?hash=ypRnsOPrqQTWm-GBTUArRQ&expires=2145884400')
        col7.write("หนังสือออกใหม่ Date a Live เล่ม 7")

        col7.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())

    # Button with a link
        if col7.button('สั่งซื้อ', key='item7', use_container_width=True):
            webbrowser.open_new_tab('https://page.line.me/sweetiess')

        # Add content to the eighth column (col8)
        col8.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 8</h2>", unsafe_allow_html=True)
        col8.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100372/title_thumbnail_portrait_list/378166.jpg?hash=-dktVpt5CIiBSFYIHAUx8Q&expires=2145884400')
        col8.write("หนังสือออกใหม่ Date a Live เล่ม 8")

        col8.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        col8.button('สั่งซื้อ', key='item8', use_container_width=True)

        # Add content to the ninth column (col9)
        col9.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 9</h2>", unsafe_allow_html=True)
        col9.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100326/title_thumbnail_portrait_list/356554.jpg?hash=Zcl4k7zGck5me9YV6T-xkw&expires=2145884400')
        col9.write("หนังสือออกใหม่ Date a Live เล่ม 9")

        col9.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        col9.button('สั่งซื้อ', key='item9', use_container_width=True)

        

        # Add content to the tenth column (col10)
        col10.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 10</h2>", unsafe_allow_html=True)
        col10.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100015/title_thumbnail_portrait_list/314380.jpg?hash=MKFL2hpxoFsBEp_KgADJpg&expires=2145884400')
        col10.write("หนังสือออกใหม่ Date a Live เล่ม 10")

        col10.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        col10.button('สั่งซื้อ', key='item10', use_container_width=True)

        # Add content to the eleventh column (col11)
        col11.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 11</h2>", unsafe_allow_html=True)
        col11.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100190/title_thumbnail_portrait_list/313078.jpg?hash=Ms-OwdDN_-SRGrQd9c8zgw&expires=2145884400')
        col11.write("หนังสือออกใหม่ Date a Live เล่ม 11")

        col11.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        col11.button('สั่งซื้อ', key='item11', use_container_width=True)

        # Add content to the twelfth column (col12)
        col12.markdown("<h2 style='text-align:center;font-size:2rem;'>Bleach Vol 12</h2>", unsafe_allow_html=True)
        col12.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100331/title_thumbnail_portrait_list/359797.jpg?hash=qta-FwX_6GBIqFvhNOeV2Q&expires=2145884400')
        col12.write("หนังสือออกใหม่ Date a Live เล่ม 12")

        col12.button('ราคา 160 บาท',use_container_width=True,type='primary',key='asdasd')
        col12.button('สั่งซื้อ', key='item12', use_container_width=True)

# Initialize session state to track page
if 'page' not in st.session_state:
    st.session_state.page = 1


if st.session_state.page == 1:
    display_page1()
    st.balloons()
elif st.session_state.page == 2:
    display_page2()
    st.balloons()

prev_col,next_col = st.columns([1,1])


with prev_col: 
    st.empty()
    previous_page = st.button('กลับ',use_container_width=100)
with next_col: 
    st.empty()
    next_page = st.button('ถัดไป',use_container_width=100)




if next_page:
    st.session_state.page = 2
elif previous_page:
    st.session_state.page = 1

# Display the page content

    

with st.sidebar:
    # ใช้ st.sidebar โดยตรง
    st.markdown('<h2 style="text-align:center;font-size:25px;">หนังสือแนะนำ</h2>',unsafe_allow_html=True)


    sug1 , sug2 = st.columns([1,1])

    sug3 , sug4 = st.columns([1,1])

    sug5 , sug6 = st.columns([1,1])


    with sug1:
            # Add content to the twelfth column (col12)
        sug1.markdown("<h5 style='text-align:center;font-size:1.2rem;'>Bleach Vol 12</h5>", unsafe_allow_html=True)
        sug1.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100169/title_thumbnail_portrait_list/315646.jpg?hash=SrZavt9Kq6wVp5wasEwhXA&expires=2145884400')
        sug1.write("หนังสือออกใหม่ Date a Live เล่ม 12")

        sug1.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        sug1.button('สั่งซื้อ', key='sug1', use_container_width=True)

    with sug2:
            # Add content to the twelfth column (col12)
        sug2.markdown("<h5 style='text-align:center;font-size:1.2rem;'>Bleach Vol 12</h5>", unsafe_allow_html=True)
        sug2.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100011/title_thumbnail_portrait_list/312388.jpg?hash=GlYOyu7QsoA8MzEVgNsgqg&expires=2145884400')
        sug2.write("หนังสือออกใหม่ Date a Live เล่ม 12")

        sug2.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        sug2.button('สั่งซื้อ', key='sug2', use_container_width=True)


    with sug3:
            # Add content to the twelfth column (col12)
        sug3.markdown("<h5 style='text-align:center;font-size:1.2rem;'>Bleach Vol 12</h5>", unsafe_allow_html=True)
        sug3.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100248/title_thumbnail_portrait_list/313420.jpg?hash=OncibJc7uVJuiTdPrOHeig&expires=2145884400')
        sug3.write("หนังสือออกใหม่ Date a Live เล่ม 12")

        sug3.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        sug3.button('สั่งซื้อ', key='sug3', use_container_width=True)

    with sug4:
            # Add content to the twelfth column (col12)
        sug4.markdown("<h5 style='text-align:center;font-size:1.2rem;'>Bleach Vol 12</h5>", unsafe_allow_html=True)
        sug4.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100331/title_thumbnail_portrait_list/359797.jpg?hash=qta-FwX_6GBIqFvhNOeV2Q&expires=2145884400')
        sug4.write("หนังสือออกใหม่ Date a Live เล่ม 12")
        sug4.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        sug4.button('สั่งซื้อ', key='sug4', use_container_width=True)


    with sug5:
            # Add content to the twelfth column (col12)
        sug5.markdown("<h5 style='text-align:center;font-size:1.2rem;'>Bleach Vol 12</h5>", unsafe_allow_html=True)
        sug5.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100321/title_thumbnail_portrait_list/349372.jpg?hash=g9t_YsWHDXQ0p0S9UgTY3Q&expires=2145884400')
        sug5.write("หนังสือออกใหม่ Date a Live เล่ม 12")
        sug5.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        sug5.button('สั่งซื้อ', key='sug5', use_container_width=True)

    with sug6:
            # Add content to the twelfth column (col12)
        sug6.markdown("<h5 style='text-align:center;font-size:1.2rem;'>Bleach Vol 12</h5>", unsafe_allow_html=True)
        sug6.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100354/title_thumbnail_portrait_list/373099.jpg?hash=KR6Z9QzbWO1T6gVwa9ao_Q&expires=2145884400')
        sug6.write("หนังสือออกใหม่ Date a Live เล่ม 12")
        sug6.button('ราคา 160 บาท',use_container_width=True,type='primary',key=uuid.uuid1())
        sug6.button('สั่งซื้อ', key='sug6', use_container_width=True)

    st.image('https://sweetiessofficial.com/wp-content/uploads/2024/07/Sweeties-Animation.gif')
    st.markdown('<h2 style="text-align:center;">ขอบคุณที่ใช้บริการค่ะ</h2>',unsafe_allow_html=True)

st.markdown('<h2 style="text-align:center;font-size:25px;">รีวิวลูกค้า</h2>',unsafe_allow_html=True)
textfield = st.text_input(label='รีวิวลูกค้า')

star = st.slider(min_value=1,max_value=5,label='⭐ ระดับความพึงพอใจ')
btn_review = st.button('แสดงความคิดเห็น',type='primary')

# แจ้งเตือน
if btn_review and star: 
    st.success('ขอบคุณสำหรับการแสดงความคิดเห็นของคุณ')
else: 
    st.error('กรุณากรอกข้อมูลให้ครบทุกช่อง')

st.markdown('<h2 style="text-align:center;font-size:25px;">ความเห็นลูกค้า</h2>',unsafe_allow_html=True)


if btn_review and star: 

    
    if star == 1: 
        st.markdown("จำนวนดาว : ⭐")
        st.error(textfield)
        st.error('😭 เสียใจจัง')
    elif star == 2:
        st.markdown("จำนวนดาว : ⭐⭐")
        st.error(textfield)
        st.error('😰 เสียใจจัง')
    elif star == 3:
        st.markdown("จำนวนดาว : ⭐⭐⭐")
        st.warning(textfield)
        st.warning('🙂 กลางๆ')
    elif star == 4:
        st.markdown("จำนวนดาว : ⭐⭐⭐⭐")
        st.success(textfield)
        st.success('😃 ดีใจ')
    elif star == 5:
        st.markdown("จำนวนดาว : ⭐⭐⭐⭐⭐")
        st.success(textfield)
        st.success('😁 ดีใจมาก')

