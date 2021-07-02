import requests
import time
import os
from selenium import webdriver
import wget
from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup as bs

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to internet\n")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def instagram_video(url):
    try:
        site = "https://igmonk.com/en/"
        driver.get(site)
        driver.find_element_by_class_name("form-control ").send_keys(url)
        driver.find_element_by_xpath("/html/body/div/center/form/input[2]").click()
        i_link=driver.find_element_by_xpath("/html/body/div/center[2]/a[1]")
        a=i_link.get_attribute('href')
        MYDIR = ("downloaded")
        CHECK_FOLDER = os.path.isdir(MYDIR)
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)
        else:
            print(MYDIR, "folder already exists.")
        label1 = Label(root, text="Start Downloading...", fg="white", bg="grey", height=2,
                      font=("Helvetica", 10))
        label1.pack(pady=5)

        wget.download(a, out=MYDIR)
        label=Label(root, text="Video Downloaded", fg="white", bg="grey", height=2,
                            font=("Helvetica", 10))
        label.pack(pady=5)
        root.after(5000, label1.destroy)
        root.after(5000, label.destroy)
    except:
        pass
def tiktok_video(url):
    try:
        site = "https://snaptik.app/"
        driver.get(site)
        driver.find_element_by_class_name("url-input").send_keys(url)
        driver.find_element_by_id("submiturl").click()
        time.sleep(5)
        t_link=driver.find_element_by_xpath('// *[ @ id = "download-block"] / div / a[1]')
        a = t_link.get_attribute('href')
        MYDIR = ("downloaded")
        CHECK_FOLDER = os.path.isdir(MYDIR)
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)
        else:
            print(MYDIR, "folder already exists.")
        label = Label(root, text="Start Downloading...", fg="white", bg="grey", height=2,
                      font=("Helvetica", 10))
        label.pack(pady=5)

        wget.download(a, out=MYDIR)
        label1 = Label(root, text="Video Downloaded", fg="white", bg="grey", height=2,
                            font=("Helvetica", 10))
        label1.pack(pady=5)
        root.after(5000, label.destroy)
        root.after(5000, label1.destroy)
    except:
        pass
def youtube_video(url):
    try:
        driver.get("https://gabed.net/iloader/")
        driver.find_element_by_id("url").send_keys(url)
        driver.find_element_by_xpath('//*[@id="send"]').click()
        time.sleep(10)
        soup = bs(driver.page_source, features="html.parser")
        element = soup.find_all("a", attrs={"class": "btn btn-info btn-sq btn-dl"})
        links = []
        for elem in element:
            l = elem["href"]
            links.append(l)
        last = links[-1]
        label = Label(root, text="Start Downloading...", fg="white", bg="grey", height=2,
                      font=("Helvetica", 10))
        label.pack(pady=5)
        root.after(5000, label.destroy)
        driver.find_element_by_xpath("//a[@href='" + last + "']").click()



    except:
        pass

def dailymotion_video(url):
    try:
        driver.get("https://gabed.net/iloader/")
        driver.find_element_by_id("url").send_keys(url)
        driver.find_element_by_xpath('//*[@id="send"]').click()
        time.sleep(10)
        soup = bs(driver.page_source, features="html.parser")
        element=soup.find_all("a",attrs={"class":"btn btn-info btn-sq btn-dl"})
        links=[]
        for elem in element:
            l=elem["href"]
            links.append(l)
        last=links[-1]
        label = Label(root, text="Start Downloading...", fg="white", bg="grey", height=2,
                      font=("Helvetica", 10))
        label.pack(pady=5)
        root.after(5000, label.destroy)
        driver.find_element_by_xpath("//a[@href='" + last + "']").click()
        # wget.download(last, out=MYDIR)

    except:
        pass



def vimeo_video(url):
    try:
        driver.get("https://gabed.net/iloader/")
        driver.find_element_by_id("url").send_keys(url)
        driver.find_element_by_xpath('//*[@id="send"]').click()
        time.sleep(10)
        soup = bs(driver.page_source, features="html.parser")
        element = soup.find_all("a", attrs={"class": "btn btn-info btn-sq btn-dl"})
        links = []
        for elem in element:
            l = elem["href"]
            links.append(l)
        last = links[-1]
        label = Label(root, text="Start Downloading...", fg="white", bg="grey", height=2,
                      font=("Helvetica", 10))
        label.pack(pady=5)
        root.after(5000, label.destroy)
        driver.find_element_by_xpath("//a[@href='" + last + "']").click()

    except:
        pass


def check_url():
    check = url_entry_box.get()

    if "youtube" in check:
        youtube_video(check)
    elif "vimeo" in check:
        vimeo_video(check)
    elif "instagram" in check:
        instagram_video(check)
    elif "tiktok" in check:
        tiktok_video(check)
    elif "dailymotion" in check:
        print("daily")
        dailymotion_video(check)
    elif check==" ":
        messagebox.showerror("Error", "Please enter URL")
    else:
        messagebox.showerror("Error", "Invalid URL is entered")
if __name__ == "__main__":

    if connection() == True:
        try:
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('headless')
            direct = os.getcwd() + "/chromedriver"
            # driver = webdriver.Chrome(executable_path=direct, options=chrome_options)
            MYDIR = ("downloaded")
            CHECK_FOLDER = os.path.isdir(MYDIR)
            if not CHECK_FOLDER:
                os.makedirs(MYDIR)
                print("created folder : ", MYDIR)
            else:
                print(MYDIR, "folder already exists.")

            Download_dir =os.getcwd()+r"\downloaded"

            preferences = {"download.default_directory": Download_dir,
                           "directory_upgrade":True}
            chrome_options.add_experimental_option("prefs", preferences)
            driver = webdriver.Chrome(executable_path=direct,options=chrome_options)


            root = Tk()
            root.title('Downloader                                                                                                                                                                        .................')
            root.geometry('600x250')
            root.configure(bg='grey')
            # root.resizable(False, False)
            heading = Label(root, text='Enter video url below', fg="white", bg="grey", height=2,
                            font=("Helvetica", 14)).pack(fill="x")
            viedos = Label(root, text='(Youtube, Instagram, Tiktok, Dailymotion, Snapchat)', fg="white", bg="grey", height=2,
                            font=("Helvetica", 10)).pack(fill="x")
            urlc = StringVar()
            url_entry_box = Entry(root, textvariable=urlc, width=40, highlightthickness=2, font=("Helvetica", 16))
            url_entry_box.pack(pady=5)
            url_startbutton = Button(root, width=12, fg="grey", text="Download", font=("Helvetica", 14),
                                     command=check_url).pack(pady=5)

            root.mainloop()

        except(KeyboardInterrupt):
            print("some error")
    else:
        messagebox.showerror("Error", "No Internet Connection")

        sys.exit()




