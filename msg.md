Iam reading oboe's documentation but don't get this text
"◆ setFramesPerDataCallback()
AudioStreamBuilder * oboe::AudioStreamBuilder::setFramesPerDataCallback	(	int	framesPerCallback	)	
inline
Request a specific number of frames for the data callback.

Default is kUnspecified. If the value is unspecified then the actual number may vary from callback to callback.

If an application can handle a varying number of frames then we recommend leaving this unspecified. This allow the underlying API to optimize the callbacks. But if your application is, for example, doing FFTs or other block oriented operations, then call this function to get the sizes you need.

Calling setFramesPerDataCallback() does not guarantee anything about timing. This just collects the data into a the number of frames that your app requires. We encourage leaving this unspecified in most cases.

If this number is larger than the burst size, some bursts will not receive a callback. If this number is smaller than the burst size, there may be multiple callbacks in a single burst.

Parameters
framesPerCallback,	
"