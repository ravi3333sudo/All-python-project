import pywhatkit as pw

txt="""python is an interpreted high-level general-purpose programming language.
Its design philosophy emphasizes code readability with its use of significant"""

pw.text_to_handwriting(txt,"text1.png",[255,0,0])
print( " END ")