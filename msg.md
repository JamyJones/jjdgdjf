Explain what -filter complex works in ffmpeg in relation to this command
ffmpeg_command = [
    'ffmpeg',
    '-i', 'input.mp3',
    '-i', 'temp.mp3',
    '-filter_complex',
    f'[1:a]adelay={delay_ms}|{delay_ms},loudnorm[voice];[0:a]loudnorm[voice]amix=inputs=2:duration=longest[audio_out]',
    '-map', '[audio_out]', 'output.mp3'
]
And why do i get the error below
[AVFilterGraph @ 0x5646865b5f40] Trailing garbage after a filter: amix=inputs=2:duration=longest[audio_out]
[AVFilterGraph @ 0x5646865b5f40] Error parsing filterchain '[0:a]loudnorm[voice]amix=inputs=2:duration=longest[audio_out]' around: amix=inputs=2:duration=longest[audio_out]
Failed to set value '[1:a]adelay=12266.0|12266.0,loudnorm[voice];[0:a]loudnorm[voice]amix=inputs=2:duration=longest[audio_out]' for option 'filter_complex': Invalid argument