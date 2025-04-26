Why is the content of the first activity not being dispalyed. My app disaplays the content  in the second  activity
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/MaterialTheme">
    <activity android:name=".CartListActivity">
    <intent-filter>
      <action android:name="android.intent.action.MAIN" />
      <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
  </activity>
  <activity
            android:exported="true"
            android:name=".ShoppingCartActivity"
            android:label="@string/app_name" >
        </activity>
    </application>
</manifest>