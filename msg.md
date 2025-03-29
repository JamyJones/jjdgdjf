What is the error in my bashcript
or index in $(seq 0 $length_pages);do
          old="${local_pages[$index]}"
          new="${remote_pages[$index]}"
          echo "old=$old, new=$new"
          sed -i "s|$old|$new|g" $filename
        done
I get `sed: -e expression #1, char 0: no previous regular expression`