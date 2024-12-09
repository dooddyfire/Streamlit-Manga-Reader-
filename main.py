import streamlit as st 
import webbrowser
import hashlib

stylesheet = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

*{
    font-family:Kanit !important;

}

</style>

"""

st.markdown(stylesheet,unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center;">ร้านหนังสือ</h1>',unsafe_allow_html=True)

st.image('https://jumpg-assets.tokyo-cdn.com/secure/top_banner/388529.jpg?hash=U-OMVZdfwmlWI1xxtQI-Zw&expires=2145884400')


st.markdown('<h2 style="text-align:center;">เกี่ยวกับเรา</h2>',unsafe_allow_html=True)

st.success('ให้บริการจำหน่ายหนังสือ มือ 2 และ มือ 1 ออนไลน์ จัดส่งฟรีทั่วประเทศไทย')

st.video('https://www.youtube.com/watch?v=gkbgz_rr4X8')

st.markdown('<h2 style="text-align:center;">สินค้าของเรา</h2>',unsafe_allow_html=True)

# 1 row
item1,item2,item3 = st.columns([1,1,1])
# 2 row
item4,item5,item6 = st.columns([1,1,1])

with item1: 

    item1.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
    item1.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100169/title_thumbnail_portrait_list/315646.jpg?hash=SrZavt9Kq6wVp5wasEwhXA&expires=2145884400')
    item1.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
    item1.button('ราคา 160 บาท',type='primary',use_container_width=100,key='1a')
    if item1.button('สั่งซื้อ',type='secondary',use_container_width=100,key='asa'):
        st.balloons()
        webbrowser.open_new_tab('https://page.line.me/sweetiess')
    

with item2: 

    item2.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
    item2.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100404/title_thumbnail_portrait_list/386681.jpg?hash=4Y2-u5mBYmgOCtLqvWo9Rw&expires=2145884400')
    item2.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
    item2.button('ราคา 180 บาท',type='primary',use_container_width=100,key='2')
    item2.button('สั่งซื้อ',type='secondary',use_container_width=100,key='3')

with item3: 

    item3.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
    item3.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100015/title_thumbnail_portrait_list/314380.jpg?hash=MKFL2hpxoFsBEp_KgADJpg&expires=2145884400')
    item3.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
    item3.button('ราคา 200 บาท',type='primary',use_container_width=100,key='4')
    item3.button('สั่งซื้อ',type='secondary',use_container_width=100,key='5')

with item4: 

    item4.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
    item4.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100015/title_thumbnail_portrait_list/314380.jpg?hash=MKFL2hpxoFsBEp_KgADJpg&expires=2145884400')
    item4.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
    item4.button('ราคา 200 บาท',type='primary',use_container_width=100,key='1923')
    item4.button('สั่งซื้อ',type='secondary',use_container_width=100,key='112')


with item5: 

    item5.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
    item5.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100015/title_thumbnail_portrait_list/314380.jpg?hash=MKFL2hpxoFsBEp_KgADJpg&expires=2145884400')
    item5.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
    item5.button('ราคา 200 บาท',type='primary',use_container_width=100,key='6')
    item5.button('สั่งซื้อ',type='secondary',use_container_width=100,key='7')

with item6: 

    item6.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
    item6.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100015/title_thumbnail_portrait_list/314380.jpg?hash=MKFL2hpxoFsBEp_KgADJpg&expires=2145884400')
    item6.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
    item6.button('ราคา 200 บาท',type='primary',use_container_width=100,key='8')
    item6.button('สั่งซื้อ',type='secondary',use_container_width=100,key='9')

st.markdown('<h2 style="text-align:center;">รีวิวลุกค้า</h2>',unsafe_allow_html=True)

text_review = st.text_input(label='รีวิวลุกค้า')
btn_submit = st.button('ส่งรีวิว',type='primary',use_container_width=100,key='10')

star = st.slider(min_value=1,max_value=5,label='จำนวนดาว')

if btn_submit: 
    if len(text_review) == 0: 
        st.error('กรุรากรอกข้อความด้วยค่ะ')
    else:
        st.success(text_review)


if star == 1: 
    st.markdown('⭐')
elif star == 2: 
    st.markdown('⭐⭐')
elif star == 3: 
    st.markdown('⭐⭐⭐')
elif star == 4: 
    st.markdown('⭐⭐⭐⭐')
elif star == 5: 
    st.markdown('⭐⭐⭐⭐⭐')



with st.sidebar: 

    st.markdown('<h2 style="text-align:center;">หนังสือแนะนำ</h2>',unsafe_allow_html=True)

    #row
    side1,side2 =  st.columns([1,1])

    with side1: 

        side1.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
        side1.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100169/title_thumbnail_portrait_list/315646.jpg?hash=SrZavt9Kq6wVp5wasEwhXA&expires=2145884400')
        side1.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
        side1.button('ราคา 160 บาท',type='primary',use_container_width=100,key='1xa')
        if side1.button('สั่งซื้อ',type='secondary',use_container_width=100,key='asxa'):
            st.balloons()
            webbrowser.open_new_tab('https://page.line.me/sweetiess')

    with side2: 

        side2.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
        side2.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100169/title_thumbnail_portrait_list/315646.jpg?hash=SrZavt9Kq6wVp5wasEwhXA&expires=2145884400')
        side2.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
        side2.button('ราคา 160 บาท',type='primary',use_container_width=100,key='1xsa')
        if side2.button('สั่งซื้อ',type='secondary',use_container_width=100,key='asxsa'):
            st.balloons()
            webbrowser.open_new_tab('https://page.line.me/sweetiess')

    #row 2  
    side3,side4 = st.columns([1,1])


    with side3: 

        side3.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
        side3.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100169/title_thumbnail_portrait_list/315646.jpg?hash=SrZavt9Kq6wVp5wasEwhXA&expires=2145884400')
        side3.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
        side3.button('ราคา 160 บาท',type='primary',use_container_width=100,key='1xxxa')
        if side3.button('สั่งซื้อ',type='secondary',use_container_width=100,key='asaxxa'):
            st.balloons()
            webbrowser.open_new_tab('https://page.line.me/sweetiess')

    with side4: 

        side4.markdown('<h4>Bleach เล่ม 1</h4>',unsafe_allow_html=True)
        side4.image('https://jumpg-assets.tokyo-cdn.com/secure/title/100169/title_thumbnail_portrait_list/315646.jpg?hash=SrZavt9Kq6wVp5wasEwhXA&expires=2145884400')
        side4.markdown('หนังสือออกใหม่ Bleach เล่ม 1')
        side4.button('ราคา 160 บาท',type='primary',use_container_width=100,key='56923')
        if side4.button('สั่งซื้อ',type='secondary',use_container_width=100,key='asxasdsa'):
            st.balloons()
            webbrowser.open_new_tab('https://page.line.me/sweetiess')