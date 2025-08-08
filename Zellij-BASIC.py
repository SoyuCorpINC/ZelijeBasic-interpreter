import os
import time
import linecache
import random
#declares the list of variables available(A-Z)
varlist = [None] * 26
gotoval = 0
ifstatementindentation = 0
filenameprog = input('Enter filename:')
os.system('cls')
pr = 0
gotoval = 0
indentationmarker = 0
def printstatement(line, pr):
    endpr = pr + 1
    if line[pr:endpr] == '"':  
        endpr = pr + 1
        while line[endpr] != '"':  
            endpr += 1
        print(line[pr + 1:endpr])
    elif line[pr + 2:endpr + 2] == '|':
        variableprintvalue = int(ord(line[pr + 1:endpr + 1])-ord('A'))
        print(varlist[variableprintvalue])
    else:
        print('No string found')
def goto(line, gotoval):
    start_line = int(gotoval)
    with open(filenameprog, 'r') as prog:
        for _ in range(start_line - 1):
            next(prog)
        readfileforstatements()
def ifstatement(line, ifs, indentationmarker):
    #handle if statements here
    ifs += 1
    global ifstatementindentation
    #string value of variable
    varvarvar = str(line[ifs - 1])
    #print('begin if statement')
    if line[ifs] == '$':
        #string setup
        ifs = ifs
        #operator
        opbeg = ifs + 2
        #print(line[opbeg])
        if line[opbeg] == '=':
            #print(line[opbeg + 2])
            if line[opbeg + 2] == '"':
                strend = opbeg + 3
                #print(line[strend])
                while line[strend] != '"':
                    strend += 1
                strval = str(line[opbeg + 3:strend])
                #print(strval)
                #print(varlist[ord(varvarvar) - ord('A')])
                if str(varlist[ord(varvarvar) - ord('A')]) == strval:
                    ifstatementindentation += 2
                    #print('if statement succeeded')
                    #print(indentationmarker, ifstatementindentation)
            elif line[opbeg + 2] == '|':
                #this marks a variable being compared to a variable
                floatvar = float(line[opbeg + 3])
                if varlist[ord(varvarvar) - ord('A')] == varlist[ord(floatvar) - ord('A')]:
                    ifstatementindentation += 2
                    #TROUBLESHOOT VARIABLE COMPARISON
            else:
                floatval = float(line[opbeg + 2:])
                if varlist[ord(varvarvar) - ord('A')] == floatval:
                    ifstatementindentation += 2
            #setup equal
        if line[opbeg] == '>':
            #print(line[opbeg + 2])
            if line[opbeg + 2] == '"':
                print('error: string cannot be compared in mathematical value to something else or another string')
            elif line[opbeg + 2] == '|':
                floatvar = float(line[opbeg + 3])
                if varlist[ord(varvarvar) - ord('A')] > varlist[ord(floatvar) - ord('A')]:
                    ifstatementindentation += 2
            else:
                floatval = float(line[opbeg + 2:])
                if varlist[ord(varvarvar) - ord('A')] > floatval:
                    ifstatementindentation += 2
        if line[opbeg] == '<':
            #print(line[opbeg + 2])
            if line[opbeg + 2] == '"':
                print('error: string cannot be compared in mathematical value to something else or another string')
            elif line[opbeg + 2] == '|':
                floatvar = line[opbeg + 3]
                if varlist[ord(varvarvar) - ord('A')] < varlist[ord(floatvar) - ord('A')]:
                    ifstatementindentation += 2
            else:
                floatval = float(line[opbeg + 2:])
                if varlist[ord(varvarvar) - ord('A')] < floatval:
                    ifstatementindentation += 2
        if line[opbeg] == '!':
            #setup not-same
            if line[opbeg + 2] == '"':
                strend = opbeg + 3
                #print(line[strend])
                while line[strend] != '"':
                    strend += 1
                strval = str(line[opbeg + 3:strend])
                #print(strval)
                #print(varlist[ord(varvarvar) - ord('A')])
                if str(varlist[ord(varvarvar) - ord('A')]) != strval:
                    ifstatementindentation += 2
                    #print('if statement succeeded')
                    #print(ifstatementindentation, indentationmarker)
            elif line[opbeg + 2] == '|':
                floatvar = line[opbeg + 3]
                #print('weve arrived')
                if varlist[ord(varvarvar) - ord('A')] != varlist[ord(floatvar) - ord('A')]:
                    ifstatementindentation += 2
                    #print('two variables being compared:')
                    #print(varlist[ord(floatvar) - ord('A')])
                    #print(varlist[ord(varvarvar) - ord('A')])
            else:
                floatval = float(line[opbeg + 2:])
                if varlist[ord(varvarvar) - ord('A')] != floatval:
                    ifstatementindentation += 2
    elif line[ifs] == '|':
        ifs = ifs
        #operator
        opbeg = ifs + 2
        #print(line[opbeg])
        #print(varvarvar)
        if line[opbeg] == '=':
            #print(line[opbeg + 2])
            if line[opbeg + 2] == '"':
                print("ERROR: numeric value assigned to variable, yet compared to string")
            elif line[opbeg + 2] == '|':
                floatvar = line[opbeg + 3]
                if float(varlist[ord(varvarvar) - ord('A')]) == float(varlist[ord(floatvar) - ord('A')]):
                    ifstatementindentation += 2
            else:
                floatval = float(line[opbeg + 2:])
                if varlist[ord(varvarvar) - ord('A')] == floatval:
                    ifstatementindentation += 2
            #setup equal
        if line[opbeg] == '>':
            #print(line[opbeg + 2])
            if line[opbeg + 2] == '"':
                print('error: string cannot be compared in mathematical value to something else or another string')
            elif line[opbeg + 2] == '|':
                #print(line[opbeg + 3])
                floatvar = line[opbeg + 3]
                if float(varlist[ord(varvarvar) - ord('A')]) > float(varlist[ord(floatvar) - ord('A')]):
                    ifstatementindentation += 2
            else:
                floatval = float(line[opbeg + 2:])
                if varlist[ord(varvarvar) - ord('A')] > floatval:
                    ifstatementindentation += 2
        if line[opbeg] == '<':
            #print(line[opbeg + 2])
            if line[opbeg + 2] == '"':
                print('error: string cannot be compared in mathematical value to something else or another string')
            elif line[opbeg + 2] == '|':
                floatvar = line[opbeg + 3]
                if float(varlist[ord(varvarvar) - ord('A')]) < float(varlist[ord(floatvar) - ord('A')]):
                    ifstatementindentation += 2
            else:
                floatval = float(line[opbeg + 2:])
                if float(varlist[ord(varvarvar) - ord('A')]) < floatval:
                    ifstatementindentation += 2
        if line[opbeg] == '!':
            #setup not-same
            if line[opbeg + 2] == '"':
                print("ERROR: numeric value assigned to variable, yet compared to string")
            elif line[opbeg + 2] == '|':
                floatvar = line[opbeg + 3]
                if float(varlist[ord(varvarvar) - ord('A')]) != float(varlist[ord(floatvar) - ord('A')]):
                    ifstatementindentation += 2
                    #print('two variables being compared:')
                    #print(varlist[ord(floatvar) - ord('A')])
                    #print(varlist[ord(varvarvar) - ord('A')])
                    #solution: make all of them floats cuz fsr they dont seem to be the same datatype
            else:
                floatval = float(line[opbeg + 2:])
                if varlist[ord(varvarvar) - ord('A')] != floatval:
                    ifstatementindentation += 2
    else:
        #print(line[ifs])
        print('incorrect if statement setup')
    #print('ifindent', ifstatementindentation)
    #print('lineindent', indentationmarker)
    #print('end if statement')
def inputstatement(line, pr):
    #print('input statement spotted')
    endpr = pr + 1
    if line[pr:endpr] == '"':  
        endpr = pr + 1
        while line[endpr] != '"':  
            endpr += 1
        try:
            if line[endpr + 1] == ',':
                varinp = str(line[endpr + 3])
                if line[endpr + 4] == '$':
                    varval = str(input(line[pr + 1:endpr]))
                #issue with the else statement, there has to be something at the spot of the $ sign, so for now | will be the number indicator
                else:
                    varval = float(input(line[pr + 1:endpr]))
                varlist[ord(varinp)-ord('A')] = varval
                #print(varlist)
        except:
            input(line[pr + 1:endpr])
            endpr = endpr
            #input(line[pr + 1:endpr])  
    else:
        print('No valid input found')
    #print('input statement ended')
def waitstatement(line, gt):
    #this is for setting up wait statements
    startwait = gt + 1
    time.sleep(float(line[startwait:]))
def clearstatement():
    os.system('cls')
def setupvariable(line, gt):
    #setup ord(variable) - ord('A') here
    global varlist
    varbegin = gt + 1
    valbegin = varbegin + 3
    valend = 0
    #in case of string
    valbeginreal = valbegin + 1
    #print(line[1:gt + 3])
    #print(line[gt + 1])
    if line[gt + 1] == '$':
        #print('string detected')
        if line[valbegin + 1] == '"':
            #print('string found')
            valend = valbeginreal + 1
            # checks string
            while line[valend] != '"':
                valend += 1
            #print(line[varbegin])
            # stores nessisary values wherever needed
            var = str(line[gt])
            val = str(line[valbeginreal + 1:valend])
            #print(val)
            varlist[ord(var)-ord('A')] = val
            #print(varlist)
        # in case of int or float
    elif line[valbegin:valbegin+4] == 'RND(':
        #assigns randomly generated number to a variable
        #print(line[valbegin:valbegin+4])
        startgen = valbegin + 4
        endgen = startgen + 1
        while line[endgen] != ';':
            endgen += 1
        firstnumber = int(line[startgen:endgen])
        newgen = endgen + 1
        finalgen = newgen + 1
        while line[finalgen] != ')':
            finalgen += 1
        secondnumber = int(line[newgen:finalgen])
        #print(firstnumber)
        #print(secondnumber)
        #input('we are here')
        var = str(line[gt])
        val = int(random.randint(firstnumber,secondnumber))
        varlist[ord(var)-ord('A')] = val
    elif line[gt + 1] != '$' and line[valbegin:valbegin+4] != 'RND(':
        valbegin = varbegin + 3
        #print(line[valbegin:])
        var = str(line[gt])
        #print("variable numeric start")
        #print(line[valbegin:])
        #
        # REQUIRE THAT INTEGERES/FLOATS USE THE | UPON DECLERATION
        #
        try:
            if line[valbegin + 1] == '|':
                var1 = line[valbegin]
                #print(line[valbegin:])
                try:
                    if line[valbegin + 3] == '+':
                        if line[valbegin + 5] == '|':
                            var2 = line[valbegin + 6]
                            var = str(line[gt])
                            varlist[ord(var)-ord('A')] = float(varlist[ord(var1)-ord('A')]) + float(varlist[ord(var2)-ord('A')])
                        else:
                            varlist[ord(var)-ord('A')] = float(varlist[ord(var1)-ord('A')]) + float(line[valbegin + 5])                    
                    elif line[valbegin + 3] == '-':
                        #print('-')
                        if line[valbegin + 5] == '|':
                            var2 = line[valbegin + 6]
                            var = str(line[gt])
                            varlist[ord(var)-ord('A')] = float(varlist[ord(var1)-ord('A')]) - float(varlist[ord(var2)-ord('A')])
                        else:
                            variablechanged = varlist[ord(var1)-ord('A')]
                            varlist[ord(var)-ord('A')] = float(variablechanged) - float(line[valbegin + 5])
                    elif line[valbegin + 3] == '*':
                        if line[valbegin + 5] == '|':
                            var2 = line[valbegin + 6]
                            var = str(line[gt])
                            varlist[ord(var)-ord('A')] = float(varlist[ord(var1)-ord('A')]) * float(varlist[ord(var2)-ord('A')])
                        else:
                            varlist[ord(var)-ord('A')] = float(varlist[ord(var1)-ord('A')]) * float(line[valbegin + 5])
                    elif line[valbegin + 3] == '/':
                        #print('divide')
                        if line[valbegin + 5] == '|':
                            var2 = line[valbegin + 6]
                            var = str(line[gt])
                            varlist[ord(var)-ord('A')] = float(varlist[ord(var1)-ord('A')]) / float(varlist[ord(var2)-ord('A')])
                        else:
                            varlist[ord(var)-ord('A')] = float(varlist[ord(var1)-ord('A')]) / float(line[valbegin + 5])
                    else:
                        print('error')
                except:
                    print('error out of range(declare singular variable)')
            else:
                #value recognition without special variables
                var = str(line[gt])
                val = float(line[gt + 4:])
                varlist[ord(var)-ord('A')] = val
        except:
            #print(line[gt + 4:])
            var = str(line[gt])
            val = float(line[gt + 4:])
            varlist[ord(var)-ord('A')] = val
            #print("variable number end")
def readfileforstatements(gotoval):
    global ifstatementindentation
    global indentationmarker
    with open(filenameprog, 'r') as prog:
        lines = prog.readlines()
    line_count = len(lines)
    current_line = 0 
    while current_line < line_count:
        global ifstatementindentation
        indentationmarker = 0
        #print(indentationmarker, ifstatementindentation)
        #print(ifstatementindentation)
        line = lines[current_line].strip()
        s = 0
        f = 1
        while line[s:f] != ']': 
            gt = f + 5
            pr = f + 6
            ifs = f + 4
            s += 1
            f += 1
            indentationmarker = 0
        # Check for INDENT MARKERS
        if line[f] == '~':
            while line[f] == '~':
                gt = f + 5
                pr = f + 6
                ifs = f + 4
                s += 1
                f += 1
                indentationmarker += 1
                #print(indentationmarker, 'line', current_line)
        #check for GOTO
        if line[f:gt] == 'GOTO' and indentationmarker == ifstatementindentation:
            ifstatementindentation = 0
            indentationmarker = 0
            gt += 1
            target_line = int(line[gt:]) - 1 
            if 0 <= target_line < line_count:
                current_line = target_line  
                continue
        if line[f:gt] == 'WAIT' and indentationmarker == ifstatementindentation:
            waitstatement(line, gt)
        # Check for LET
        if line[f:gt] == 'LET ' and indentationmarker == ifstatementindentation:
            setupvariable(line, gt)
        # Check for PRINT
        if line[f:pr] == 'PRINT' and indentationmarker == ifstatementindentation:
            printstatement(line, pr)
        if line[f:pr] == 'CLEAR' and indentationmarker == ifstatementindentation:
            clearstatement()
        # Check for INPUT
        if line[f:pr] == 'INPUT' and indentationmarker == ifstatementindentation:
            inputstatement(line, pr)
        if line[f:ifs] == 'IF ' and indentationmarker == ifstatementindentation:
            ifstatement(line, ifs, indentationmarker)
        if line[f:ifs + 2] == 'ENDIF' and indentationmarker == ifstatementindentation - 2 and ifstatementindentation != 0:
            #print('ENDIF found')
            indentationmarker -= 2
            ifstatementindentation -= 2
        else:
            indentationmarker = indentationmarker 
        current_line += 1
        #print(line[f:ifs + 2])
        #print('ifstatement: ',ifstatementindentation)
        #print('indentationmarker: ',indentationmarker)
    print("Program finished.")
readfileforstatements(gotoval)
    

