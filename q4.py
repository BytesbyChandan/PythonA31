class writer:
    def write():
        print("Writing to file...")
class speaker:
    def speak():
        print("Speaking...")
class author(writer, speaker):
    def all_method_call(self):
        writer.write()
        speaker.speak()
au = author()
au.all_method_call()
