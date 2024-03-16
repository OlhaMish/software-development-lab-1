from markdown_to_html.text_processing import process_text


def test_primitive():
    expected_result = "And <b>bold text</b> <b>gg</b> , <i>ita_li_cs_tex_t</i>, hgf and even <tt>monospaced text</tt>,"
    input_markdown = "And **bold text** **gg** , _ita_li_cs_tex_t_, hgf and even `monospaced text`,"

    result = process_text(input_markdown)

    assert expected_result == result
