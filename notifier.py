from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast(
    "Whatsapp",
    "You have received new messages",
    duration=5,
)
