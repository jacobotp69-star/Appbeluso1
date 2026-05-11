import os
import shutil

src = r'f:\conrutas\AppBeluso\dist'
dst = r'f:\conrutas\AppBeluso\android\app\src\main\assets\public'

def copy_recursive(s, d):
    if not os.path.exists(d):
        try:
            os.makedirs(d)
        except:
            print(f"Could not create directory {d}, skipping but trying children...")
    
    for item in os.listdir(s):
        s_item = os.path.join(s, item)
        d_item = os.path.join(d, item)
        if os.path.isdir(s_item):
            copy_recursive(s_item, d_item)
        else:
            try:
                shutil.copy2(s_item, d_item)
                # print(f"Copied {item}")
            except Exception as e:
                print(f"Error copying {item}: {e}")

copy_recursive(src, dst)
print("Finished manual copy to android assets")
