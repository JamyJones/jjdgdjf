This command works but takes too long, explain why it is so 
ffmpeg_command = [
    'ffmpeg',
    '-i', 'input.mp3',
    '-i', 'temp.mp3',
    '-filter_complex',
    f'[1:a]adelay={delay_ms}|{delay_ms},loudnorm[delayed];'
    f'[0:a]loudnorm[base];'
    f'[base][delayed]amix=inputs=2:duration=longest[audio_out]',
    '-map', '[audio_out]', 'output.mp3'
]