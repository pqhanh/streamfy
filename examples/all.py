import streamlit as st
import streamfy as sy

st.title("Streamfy — Bulma for Streamlit")
st.write("""
This gallery showcases modern controls implemented in https://github.com/hal9ai/streamfy 
""")

st.subheader("Breadcrumb")
item = sy.breadcrumb(items=[{"text": "A"}, {"text": "B"}])
st.write(item)

st.subheader("Button")
if sy.button(text = "Primary", type="is-primary"):
    st.write("Clicked!")

sy.button(text = "Primary Light", type="is-primary is-light")
sy.button(text = "Success", type="is-success")
sy.button(text = "Success Light", type="is-success is-light")
sy.button(text = "Danger", type="is-danger")
sy.button(text = "Danger Light", type="is-danger is-light")
sy.button(text = "Warning", type="is-warning")
sy.button(text = "Warning Light", type="is-warning is-light")
sy.button(text = "Info", type="is-info")
sy.button(text = "Info Light", type="is-info is-light") 
sy.button(text = "Link", type="is-link")
sy.button(text = "Link Light", type="is-link is-light") 
sy.button(text = "Light", type="is-light")
sy.button(text = "Ghost", type="is-ghost")

st.subheader("Carousel")
selection = sy.carousel(items=[
    "https://picsum.photos/id/1051/1230/500",
    "https://picsum.photos/id/1052/1230/500",
    "https://picsum.photos/id/1053/1230/500",
])
st.write(selection)

st.subheader("Autocomplete")
complete = sy.autocomplete(data=["Apple", "Bannana", "Cherry"])
st.write(complete)

st.subheader("Checkbox")
checked = sy.checkbox(text="Check me")
st.write(checked)

sy.checkbox(text="Info", type="is-info", default=True)
sy.checkbox(text="Success", type="is-success", default=True)
sy.checkbox(text="Danger", type="is-danger", default=True)
sy.checkbox(text="Warning", type="is-warning", default=True)

st.subheader("Clockpicker")
clock = sy.clockpicker()
st.write(clock)

st.subheader("Colorpicker")
color = sy.colorpicker()
st.write(color)

st.subheader("Datepicker")
datepick = sy.datepicker()
st.write(datepick)

st.subheader("Input")
text = sy.input()
st.write(text)

sy.input(type="email", icon="email", default="john@", maxlength="30")
sy.input(type="is-success", maxlength="30")
sy.input(type="password", value="iwantmytreasure", password_reveal=True)
sy.input(type="textarea", maxlength="200")
sy.input(label="Success", type="is-success")
sy.input(label="Error", type="is-danger")
sy.input(label="Info", type="is-info")
sy.input(label="Warning", type="is-warning")

st.subheader("Numberinput")
number = sy.numberinput(placeholder="10", min="5")
st.write(number)

st.subheader("Radio")
radio = sy.radio(radios=[{"text": "A"}, {"text": "B"}])
st.write(radio)

st.subheader("Rate")
rate = sy.rate()
st.write(rate)

st.subheader("Select")
selected = sy.select(data=[{"text": "Seattle"},{"text": "Portland"}])
st.write(selected)

st.subheader("Slider")
slide = sy.slider()
st.write(slide)

st.subheader("Switch")
switched = sy.switch(text="Switch me!")
st.write(switched)

st.subheader("Tags")
tags = sy.taginput(data=["A", "B", "C"], default=["B"], allow_new=True, open_on_focus=True, type="is-info", aria_close_label="Remove", placeholder="Choose letter")
st.write(tags)

st.subheader("Message")
sy.message(text="This is a message", title="Info", type="is-info")

st.subheader("Notification")
sy.notification(text="Important notification")

st.subheader("Progress")
sy.progress(value=80)

st.subheader("Steps")
sy.steps(steps=[
    {"step": "1", "label": "First"},
    {"step": "2", "label": "Second"}
])

st.subheader("Table")
columns = [
    {
        "field": 'id',
        "label": 'ID',
        "width": '40',
        "numeric": True
    },
    {
        "field": 'name',
        "label": 'Name',
    },
]
data = [
    { 'id': 1, 'name': 'Jesse' },
    { 'id': 2, 'first_name': 'John' },
]
sy.table(data=data, columns=columns, paginated=True)