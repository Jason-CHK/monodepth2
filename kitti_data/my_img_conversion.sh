for img in ./2011_09_29/*/*/*/*.png; do
    filename=${img%.*}
    magick convert -quality 92 -sampling-factor 2x2,1x1,1x1 "$filename.png" "$filename.jpg" && rm "$filename.png"
done