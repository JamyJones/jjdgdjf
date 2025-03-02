Explain what is going on below
ffmpeg_command = [
    'ffmpeg',
    '-i', 'input.mp3',
    '-i', 'temp.mp3',
    '-filter_complex',
    f'[1:a]adelay={delay_ms}|{delay_ms},loudnorm[voice];[0:a]loudnorm[voice];[voice]amix=inputs=2:duration=longest[audio_out]',
    '-map', '[audio_out]',
    'output.mp3'
]