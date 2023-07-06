from tkinter import*
import speedtest
root=Tk()
root.geometry("400x400")
root.config(bg="lightgreen")
root.title("Prueba de velocidad ")


label = Label(root, text="Prueba de velocidad", font=("Lucida Sans Unicode", 22, "bold","italic"), fg="#5D6D7E", bg="#dee8f1")
label.place(relx=0.5, rely=0.1,anchor=CENTER)

label_download = Label(root ,text="Velocidad de descarga ↓", font=("Segoe Print", 18, "bold"), fg="#1E8449", bg="#dee8f1")
label_download.place(relx=0.25, rely=0.5,anchor=CENTER)
label_upload = Label(root,text="Velocidad de respuesta ↑", font=("Segoe Print", 18, "bold"), fg="#9B59B6", bg="#dee8f1")
label_upload.place(relx=0.75, rely=0.5,anchor=CENTER)

label_download_speed = Label(root , font=("Yu Gothic Light", 14, "bold"), bg="#dee8f1")
label_download_speed.place(relx=0.25, rely=0.6,anchor=CENTER)

label_upload_speed = Label(root , font=("Yu Gothic Light", 14, "bold"), bg="#dee8f1")
label_upload_speed.place(relx=0.75, rely=0.6,anchor=CENTER)

def a():
    st = speedtest.Speedtest()
    velo1=round(st.download()/1000000,2)
    label_download_speed["text"]=str(velo1) + "MBS"
    velo2=round(st.upload()/1000000,2)
    label_upload_speed["text"]=str(velo2) + "MBS"

button1=Button(root,text="Dame click para hacer la prueba",font=("Segoe Print",18,"bold"),fg="#1E8449",bg="#dee8f1",command=a)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()