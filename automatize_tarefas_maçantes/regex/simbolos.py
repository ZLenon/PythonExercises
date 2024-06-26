"""
Revisão dos símbolos de regex
Este capítulo discutiu bastante a notação; sendo assim, apresentaremos uma
revisão rápida do que aprendemos:
• ? corresponde a zero ou uma ocorrência do grupo anterior.
• * corresponde a zero ou mais ocorrências do grupo anterior.
• + corresponde a uma ou mais ocorrências do grupo anterior.
• {n} corresponde a exatamente n ocorrências do grupo anterior.
• {n,} corresponde a n ou mais ocorrências do grupo anterior.
• {,m} corresponde a zero até m ocorrências do grupo anterior.
• {n,m} corresponde a no mínimo n e no máximo m ocorrências do grupo
anterior.
• {n,m}? ou *? ou +? faz uma correspondência nongreedy do grupo anterior.
• ^spam quer dizer que a string deve começar com spam.
• spam$ quer dizer que a string dever terminar com spam.
• . corresponde a qualquer caractere, exceto os caracteres de quebra de linha.
• \d, \w e \s correspondem a um dígito, um caractere de palavra ou um
caractere de espaço, respectivamente.
• \D, \W e \S correspondem a qualquer caractere, exceto um dígito, um
caractere de palavra ou um caractere de espaço, respectivamente.
• [abc] corresponde a qualquer caractere que estiver entre os colchetes (por
exemplo, a, b ou c).
• [^abc] corresponde a qualquer caractere que não esteja entre os colchetes.
"""
