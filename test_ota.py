from ota import OTAUpdater
from secrets import wifi_ssid, wifi_pw

firmware_url = "https://github.com/axeldelaguardia/ota_test/"

ota_updated = OTAUpdater(wifi_ssid, wifi_pw, firmware_url, "main.py")

ota_updated.download_and_install_update_if_available()