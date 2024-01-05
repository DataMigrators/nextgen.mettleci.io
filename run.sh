#!/bin/bash

set -x

# Specify the directory containing the Markdown files
directory=$1

# Loop through each Markdown file in the directory
for file in $directory/*.md; do
  echo "Processing $file..."

  # Get the filename without the directory path or file extension
  filename=$(basename "$file" .md)

  if [ $directory == $filename ]; then
    echo Skipping index page $filename
    continue
  fi

  cp $file $file.orig

  echo Writing "$directory/$filename.md"

  # Add the Jekyll front matter to the start of the file

  echo "---" > "$directory/$filename.md"
  echo "layout: page" >> "$directory/$filename.md"
  echo "title: $filename" >> "$directory/$filename.md"
  echo "parent: $directory" >> "$directory/$filename.md"
  echo "---" >> "$directory/$filename.md"
  echo "" >> "$directory/$filename.md"
  cat "$file.orig" >> "$directory/$filename.md"

  # Remove the original Markdown file
  # rm "$file.orig"

done

