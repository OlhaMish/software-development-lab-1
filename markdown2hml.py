from markdown_to_html.text_processing import process_text


try:
    res = process_text('hufh **idi')
    for part in res:
        print(part)
except ValueError as e:
    print("Error: ", e)
