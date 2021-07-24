import configparser, sys
def main():
    config = configparser.ConfigParser()
    config.add_section("URL")
    config.add_section("Settings")
    config.add_section("Extentions")
    config.set("URL", "opera-google", 'url|https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes&utm_source=yandex_via_opera_com&utm_medium=ba_ose&utm_campaign=RUSSIA_BRAND_Search_via_opera_com_https&&&http_referrer=missing_via_opera_com&utm_site=opera_com&&utm_lastpage=opera.com/computer&dl_token=14586610|exe|base')
    config.set("URL", "opera-yandex", 'url|https://net.geo.opera.com/opera/stable/windows?edition=Yx+05&utm_tryagain=yes&utm_source=yandex_via_opera_com&utm_medium=ba_ose&utm_campaign=RUSSIA_BRAND_Search_via_opera_com_https&&&http_referrer=https%%3A%%2F%%2Fwww.opera.com%%2Fru%%2%%Fcomputer%%2Fthanks%%3Fni%%3Dstable%%26os%%3Dwindows&utm_site=opera_com&&utm_lastpage=opera.com/computer&dl_token=65240017|exe|base')
    config.set("URL", "opera", "link|opera-google")
    config.set("URL", "chrome", "url|https://dl.google.com/tag/s/appguid%%3D%%7B8A69D345-D564-463C-AFF1-A69D9E530F96%%7D%%26iid%%3D%%7B09D295D5-9465-850B-0222-221392D03FF0%%7D%%26lang%%3Dru%%26browser%%3D4%%26usagestats%%3D1%%26appname%%3DGoogle%%2520Chrome%%26needsadmin%%3Dprefers%%26ap%%3Dx64-stable-statsdef_1%%26installdataindex%%3Dempty/update2/installers/ChromeSetup.exe|exe|base")
    config.set("URL", "viber", "url|https://download.cdn.viber.com/desktop/windows/ViberSetup.exe|exe|base")
    config.set("URL", "roblox", "url|https://setup.rbxcdn.com/version-7d96d7dad25d49f1-Roblox.exe|exe|base")
    config.set("URL", "vlc", "url|https://mirror.yandex.ru/mirrors/ftp.videolan.org/vlc/3.0.14/win64/vlc-3.0.14-win64.exe|exe|base")
    config.set("URL", "spotify", "url|https://download.scdn.co/SpotifySetup.exe|exe|base")
    config.set("URL", "yandex-disk", "url|https://downloader.disk.yandex.ru/share/eb251781b7ee9fc17772fd207e065076d41196888252e9ece40afd473fb1415b/60c7d63f/9xkN1FNhMUESNsSeLaNR0TubeZ7cDNuKjtsZye8Xc10591KfQMjnKGgixx8AZaI35uNSqajohlSxswFPSfiVSA%%3D%%3D?src=Yandex.Landing&hash=&uid=0&owner_uid=0&fsize=1957176&filename=YandexDisk30Setup.exe&disposition=attachment&tknv=v2&limit=0&etag=416805bcc11b9008585c05c733fcc89a&content_type=application%%2Fx-dosexec&media_type=executable&hid=3fd546b4ecb2877bc2364524aad9d0d3|exe|base")
    config.set("URL", "yandex-browser", "url|https://cache-mskstoredata11.cdn.yandex.net/download.cdn.yandex.net/browser/yandex/21_5_3_740_23113/ru/lite/Yandex.exe?win10pin=1&vup=1&browser=OperaChrome/64/76.0.4017.177&abtup=1&banerid=5000004765:60c79e7bdefcc5001e661e71&statpromo=true&pps=installID%%3D4598004541623003045_1623694971276&yandexuid=4598004541623003045&hash=913f6b16b2f9bf93d1911b79b94fc625&download_date=1623694971&.exe|exe|base")
    config.set("URL", "bluestacks", "url|https://cdn3.bluestacks.com/downloads/windows/nxt/5.0.220.2101/0c19704b2112a66da2f055562077bdfb/BlueStacksMicroInstaller_5.0.220.2101_native.exe?filename=BlueStacksInstaller_5.0.220.2101_native_d52cb45b46a0f607fcd6b236e415cda7_0.exe|exe|base")
    config.set("URL", "blender", "url|https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.93/blender-2.93.0-windows-x64.msi|msi|base")
    config.set("URL", "gimp", "url|https://mirrors.dotsrc.org/gimp/gimp/v2.10/windows/gimp-2.10.24-setup-3.exe|exe|base")
    config.set("URL", "notepadpp", "url|https://github-releases.githubusercontent.com/33014811/885b3080-c72f-11eb-9af7-defe652549a1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%%2F20210614%%2Fus-east-1%%2Fs3%%2Faws4_request&X-Amz-Date=20210614T190736Z&X-Amz-Expires=300&X-Amz-Signature=af1ccdf3413d0250bdd9681c6082913ea9c11dea93bd800b45027133eea00d6f&X-Amz-SignedHeaders=host&actor_id=71311338&key_id=0&repo_id=33014811&response-content-disposition=attachment%%3B%%20filename%%3Dnpp.8.0.Installer.exe&response-content-type=application%%2Foctet-stream|exe|base")
    config.set("URL", "atom", "url|https://atom-installer.github.com/v1.57.0/AtomSetup-x64.exe?s=1620674356&ext=.exe|exe|base")
    config.set("URL", "totalcmd", "url|https://totalcommander.ch/win/tcmd1000x32_64.exe|exe|base")
    config.set("URL", "utorrent", "url|https://download-hr.utorrent.com/track/stable/endpoint/utorrent/os/windows|exe|base")
    config.set("URL", "qbittorrent", "url|https://deac-riga.dl.sourceforge.net/project/qbittorrent/qbittorrent-win32/qbittorrent-4.3.5/qbittorrent_4.3.5_x64_setup.exe|exe|base")
    config.set("URL", "directx", "url|https://download.microsoft.com/download/1/7/1/1718CCC4-6315-4D8E-9543-8E28A4E18C4C/dxwebsetup.exe|exe|base")
    config.set("URL", ".net", "url|https://download.microsoft.com/download/9/5/A/95A9616B-7A37-4AF6-BC36-D6EA96C8DAAE/dotNetFx40_Full_x86_x64.exe|exe|base")
    config.set("URL", "vs-code", "url|https://az764295.vo.msecnd.net/stable/b4c1bd0a9b03c749ea011b06c6d2676c8091a70c/VSCodeUserSetup-x64-1.57.0.exe|exe|base")
    config.set("URL", "visualstudio", "url|https://visualstudio.microsoft.com/01b23d4c-b467-40a3-aefa-bd049f286320|exe|base")
    config.set("URL", "discord", "url|https://dl.discordapp.net/distro/app/stable/win/x86/1.0.9002/DiscordSetup.exe|exe|base")
    config.set("URL", "zoom", "url|https://cdn.zoom.us/prod/5.6.7.1016/ZoomInstaller.exe|exe|base")
    config.set("URL", "fs-viewer", "url|https://www.faststonesoft.net/DN/FSViewerSetup75.exe|exe|base")
    config.set("URL", "python3", "url|https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe|exe|base")
    config.set("URL", "python2", "url|https://www.python.org/ftp/python/2.7.18/python-2.7.18.amd64.msi|msi|base")
    config.set("URL", "python", "link|python3")
    config.set("URL", "golang", "url|https://dl.google.com/go/go1.16.5.windows-amd64.msi|msi|base")
    config.set("URL", "go", "link|golang")
    config.set("URL", "avast", "url|https://install.avcdn.net/iavs9x/avast_free_antivirus_setup_online.exe|exe|base")
    config.set("URL", "bandicam", "url|https://dl.bandicam.com/bdcamsetup.exe|exe|base")
    path = "../data/config.ini"
    if len(sys.argv) == 2:
        path = sys.argv[1]
    with open(path, "w") as f:
        config.write(f)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        input()