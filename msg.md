Why is the Orientation not changing to landscape given i have Specified it in my AndroidManifest.xml
<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" android:compileSdkVersion="30" android:compileSdkVersionCodename="11" android:hardwareAccelerated="true" package="com.readEra" platformBuildVersionCode="30" platformBuildVersionName="11">
    <supports-screens android:anyDensity="true" android:largeScreens="true" android:normalScreens="true" android:resizeable="true" android:smallScreens="true" android:xlargeScreens="true"/>             <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.WAKE_LOCK"/>    <uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>                                                             <uses-permission android:name="android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS"/>                                           <application android:appComponentFactory="androidx.core.app.CoreComponentFactory" android:debuggable="true" android:hardwareAccelerated="true" android:icon="@mipmap/ic_launcher" android:label="@string/app_name" android:supportsRtl="true" android:screenOrientation="landscape" >
        <activity android:configChanges="keyboard|keyboardHidden|locale|orientation|screenLayout|screenSize|smallestScreenSize|uiMode" android:exported="true" android:label="@string/activity_name" android:launchMode="singleTop" android:name="com.pomodoro.MainActivity" android:theme="@style/Theme.AppCompat.NoActionBar" android:windowSoftInputMode="adjustResize">
            <intent-filter android:label="@string/launcher_name">                 <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>                                                       <service android:name="de.appplant.cordova.plugin.background.ForegroundService"/>
    </application>
</manifest>