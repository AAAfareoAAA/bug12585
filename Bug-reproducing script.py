# coding: utf-8
#
import uiautomator2 as u2

d = u2.connect()

d(resourceId="com.miui.home:id/icon_icon", description="AnkiDroid").click()
#需要下滑开启控制栏
d(resourceId="miui.systemui.plugin:id/status_icon", description="WLAN,开启,WLAN 信号满格。,铭记1和9").click()
d(resourceId="com.ichi2.anki:id/action_sync").click()
d(resourceId="com.ichi2.anki:id/md_button_positive").click()