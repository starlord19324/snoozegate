# Ця програма створена для кодування тексту в абетку Морзе
# Для використання потрібно обрати 1 (код морзе у текст) або 2 (текст у код морзе)
# q - вихід
# Потрібно використовувати літери українського алфавіту або цифри
# Copyright Anton Kharchenko, 2020 
def morse_text():
    print('q - вихід')
    morse_table = []
    while True:
        string = str(input('Введіть код Морзе (1 символ): '))
        if string == ('q'):
            break
        elif string == '.-':
            morse_code = ('а')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.......':
            morse_code = (' ')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-...':
            morse_code = ('б')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.--':
            morse_code = ('в')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '....':
            morse_code = ('г')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '−−.':
            morse_code = ('ґ')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-..':
            morse_code = ('д')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.':
            morse_code = ('е')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '..−..':
            morse_code = ('є')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '...-':
            morse_code = ('ж')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '--..•':
            morse_code = ('з')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '−.−−':
            morse_code = ('и')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '..':
            morse_code = ('і')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.−−−.':
            morse_code = ('ї')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-.-':
            morse_code = ('к')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.-..':
            morse_code = ('л')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '--':
            morse_code = ('м')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-.':
            morse_code = ('н')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '---':
            morse_code = ('о')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.--.':
            morse_code = ('п')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.-.':
            morse_code = ('р')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '...':
            morse_code = ('с')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-':
            morse_code = ('т')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '..-':
            morse_code = ('у')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '..-.':
            morse_code = ('ф')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '....':
            morse_code = ('х')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-.-.':
            morse_code = ('ц')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '---':
            morse_code = ('ц')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '----':
            morse_code = ('ш')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '--.-':
            morse_code = ('щ')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '..--':
            morse_code = ('ю')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.-.-':
            morse_code = ('я')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.----':
            morse_code = ('1')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '..---':
            morse_code = ('2')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '...--':
            morse_code = ('3')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '....-':
            morse_code = ('5')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.....':
            morse_code = ('5')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-....':
            morse_code = ('6')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '--...':
            morse_code = ('7')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '---..•':
            morse_code = ('8')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '----.':
            morse_code = ('9')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-----':
            morse_code = ('0')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '......':
            morse_code = ('. ')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.-.-.-':
            morse_code = (', ')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '---...':
            morse_code = (':')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-.-.-':
            morse_code = (';')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-.--.-':
            morse_code = ('(')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-.--.-':
            morse_code = (')')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.-..-.':
            morse_code = ('"')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '..--..':
            morse_code = ('?')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '--..--':
            morse_code = ('!')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.--.-.':
            morse_code = ('@')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '-....-':
            morse_code = ('-')
            print(morse_code)
            morse_table.append(morse_code)
        elif string == '.......':
            morse_code = (' ')
            print(morse_code)
            morse_table.append(morse_code)

    print(morse_table)
    morse_table = ''.join(morse_table)
    print('Одним реченням: ', morse_table)

def text_morse():
    text = []
    text = str(input('Введіть текст: ')).lower()
    print(text)
    morse = []
    for string in text:
        if string == 'а':
            morse_code = ('• —')
            print(morse_code)
            morse.append(morse_code)
        elif string == 'б':
            morse_code = ('— • • •')
            print('— • • •')
            morse.append(morse_code)
        elif string == 'в':
            morse_code = ('• — —')
            print('• — —')
            morse.append(morse_code)
        elif string == 'г':
            morse_code = ('• • • •')
            print('— — •')
        elif string == 'ґ':
            morse_code = ('— — •')
            print('— — •')
            morse.append(morse_code)
        elif string == 'д':
            morse_code = ('— • •')
            print('— • •')
            morse.append(morse_code)
        elif string == 'е':
            morse_code = ('• ')
            print('• ')
        elif string == 'є':
            morse_code = ('• • - • •')
            print('• • - • •')
            morse.append(morse_code)
        elif string == 'ж':
            morse_code = ('• • • —')
            print('• • • —')
            morse.append(morse_code)
        elif string == 'з':
            morse_code = ('— — • •')
            print('— — • •')
            morse.append(morse_code)
        elif string == 'и':
            morse_code = ('- • - -')
            print('- • - -')
        elif string == 'і':
            morse_code = ('• •')
            print('• •')
            morse.append(morse_code)
        elif string == 'ї':
            morse_code = ('- • -')
            print('- • -')
            morse.append(morse_code)
        elif string == 'к':
            morse_code = ('— • —')
            print('— • —')
            morse.append(morse_code)
        elif string == 'л':
            morse_code = ('• — • •')
            print('• — • •')
            morse.append(morse_code)
        elif string == 'м':
            morse_code = ('— —')
            print('— —')
            morse.append(morse_code)
        elif string == 'н':
            morse_code = ('— •')
            print('— •')
            morse.append(morse_code)
        elif string == 'о':
            morse_code = ('— — —')
            print('— — —')
            morse.append(morse_code)
        elif string == 'п':
            morse_code = ('• — — •')
            print('• — — •')
            morse.append(morse_code)
        elif string == 'р':
            morse_code = ('• — •')
            print('• — •')
            morse.append(morse_code)
        elif string == 'с':
            morse_code = ('• • •')
            print('• • •')
            morse.append(morse_code)
        elif string == 'т':
            morse_code = ('—')
            print('—')
            morse.append(morse_code)
        elif string == 'у':
            morse_code = ('• • —')
            print('• • —')
            morse.append(morse_code)
        elif string == 'ф':
            morse_code = ('• • — •')
            print('• • — •')
            morse.append(morse_code)
        elif string == 'х':
            morse_code = ('• • • •')
            print('• • • •')
            morse.append(morse_code)
        elif string == 'ц':
            morse_code = ('— • — •')
            print('— • — •')
            morse.append(morse_code)
        elif string == 'ч':
            morse_code = ('— — — ')
            print('— — — •')
            morse.append(morse_code)
        elif string == 'ш':
            morse_code = ('— — — —')
            print('— — — —')
            morse.append(morse_code)
        elif string == 'щ':
            morse_code = ('— — • —')
            print('— — • —')
            morse.append(morse_code)
        elif string == 'ь':
            morse_code = ('— • • —')
            print('— • • —')
            morse.append(morse_code)
        elif string == 'ю':
            morse_code = ('• • — —')
            print('• • — —')
            morse.append(morse_code)
        elif string == 'я':
            morse_code = ('• — • —')
            print('• — • —')
            morse.append(morse_code)
        elif string == '1':
            morse_code = ('• — — — —')
            print('• — — — —')
            morse.append(morse_code)
        elif string == '2':
            morse_code = ('• • — — —')
            print('• • — — —')
            morse.append(morse_code)
        elif string == '3':
            morse_code = ('• • • — —')
            print('• • • — —')
            morse.append(morse_code)
        elif string == '4':
            morse_code = ('• • • • —')
            print('• • • • —')
            morse.append(morse_code)
        elif string == '5':
            morse_code = ('• • • • •')
            print('• • • • •')
            morse.append(morse_code)
        elif string == '6':
            morse_code = ('— • • • •')
            print('— • • • •')
            morse.append(morse_code)
        elif string == '7':
            morse_code = ('— — • • •')
            print('— — • • •')
            morse.append(morse_code)
        elif string == '8':
            morse_code = ('— — — • •')
            print('— — — • •')
            morse.append(morse_code)
        elif string == '9':
            morse_code = ('— — — — •')
            print('— — — — •')
            morse.append(morse_code)
        elif string == '0':
            morse_code = ('— — — — —')
            print('— — — — —')
            morse.append(morse_code)
        elif string == '.':
            morse_code = ('• • • • • •')
            print('• • • • • •')
            morse.append(morse_code)
        elif string == ',':
            morse_code = ('• — • — • —')
            print('• — • — • —')
            morse.append(morse_code)
        elif string == ':':
            morse_code = ('— — — • • •')
            print('— — — • • •')
            morse.append(morse_code)
        elif string == ';':
            morse_code = ('— • — • —')
            print('— • — • —')
            morse.append(morse_code)
        elif string == '(':
            morse_code = ('— • — — • —')
            print('— • — — • —')
            morse.append(morse_code)
        elif string == ')':
            morse_code = ('— • — — • —')
            print('— • — — • —')
            morse.append(morse_code)
        elif string == '"':
            morse_code = ('• — • • — •')
            print('• — • • — •')
            morse.append(morse_code)
        elif string == '?':
            morse_code = ('• • — — • •')
            print('• • — — • •')
            morse.append(morse_code)
        elif string == '!':
            morse_code = ('— — • • — —')
            print('— — • • — —')
            morse.append(morse_code)
        elif string == '@':
            morse_code = ('• — — • — •')
            print('• — — • — •')
            morse.append(morse_code)
        elif string == '-':
            morse_code = ('— • • • • —')
            print('— • • • • —')
            morse.append(morse_code)
        elif string == ' ':
            morse_code = ('.......')
            print('.......')
            morse.append(morse_code)

    morse = ''.join(morse)
    print('Одним реченням: ', morse)

def choice():
    choice = str(input(' З тексту в код Морзе - 1\n З коду Морзе в текст - 2\n'))
    if choice == '1':
        text_morse()
    elif choice == '2':
        morse_text()

choice()
