letras_grandes = {
    'A': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
    'B': ['**** ', '*   *', '**** ', '*   *', '**** '],
    'C': [' ****', '*    ', '*    ', '*    ', ' ****'],
    'D': ['**** ', '*   *', '*   *', '*   *', '**** '],
    'E': ['*****', '*    ', '*****', '*    ', '*****'],
    'F': ['*****', '*    ', '**** ', '*    ', '*    '],
    'G': [' ****', '*    ', '* ***', '*   *', ' ****'],
    'H': ['*   *', '*   *', '*****', '*   *', '*   *'],
    'I': ['*****', '  *  ', '  *  ', '  *  ', '*****'],
    'J': ['*****', '    *', '    *', '*   *', ' *** '],
    'K': ['*   *', '*  * ', '***  ', '*  * ', '*   *'],
    'L': ['*    ', '*    ', '*    ', '*    ', '*****'],
    'M': ['*   *', '** **', '* * *', '*   *', '*   *'],
    'N': ['*   *', '**  *', '* * *', '*  **', '*   *'],
    'O': [' *** ', '*   *', '*   *', '*   *', ' *** '],
    'P': ['**** ', '*   *', '**** ', '*    ', '*    '],
    'Q': [' *** ', '*   *', '*   *', '*  **', ' ** *'],
    'R': ['**** ', '*   *', '**** ', '*  * ', '*   *'],
    'S': [' ****', '*    ', ' *** ', '    *', '**** '],
    'T': ['*****', '  *  ', '  *  ', '  *  ', '  *  '],
    'U': ['*   *', '*   *', '*   *', '*   *', ' *** '],
    'V': ['*   *', '*   *', '*   *', ' * * ', '  *  '],
    'W': ['*   *', '*   *', '* * *', '** **', '*   *'],
    'X': ['*   *', ' * * ', '  *  ', ' * * ', '*   *'],
    'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
    'Z': ['*****', '   * ', '  *  ', ' *   ', '*****'],
    ' ': ['     ', '     ', '     ', '     ', '     ']
}

mensaje = "urmy eternal wish mirian"
for i in range(5):
    for letra in mensaje:
        print(letras_grandes[letra.upper()][i], end='  ')
    print()