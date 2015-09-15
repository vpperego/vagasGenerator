from tkinter import Frame, Tk, BOTH, Text, Menu, END
import tkinter.filedialog
import tkinter.messagebox
import nltk
class Janela(Frame):
    json.loads(unicode(opener.open(...), "ISO-8859-1"))
    modoSaida=None
    textoEntrada=None
    tokens= nltk.tokenize
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Vagas Generator")
        self.pack(fill=BOTH, expand=1)
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar,tearoff=0)
        fileMenu.add_command(label="Abrir", command=self.onOpen)
        fileMenu.add_command(label="Salvar", command=self.onSave)
        ajuda = Menu(menubar,tearoff=0)
        ajuda.add_command(label="Como usar", command=self.uso)
        ajuda.add_command(label="Sobre", command=self.sobre)
        menubar.add_cascade(label="Arquivo", menu=fileMenu)
        menubar.add_cascade(label="Ajuda",menu=ajuda)
        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)
    def uso(self):
        tkinter.messagebox.showinfo("Como usar", "Coloque o texto de entrada no bloco de notas, removendo todas as linhas em branco para salvar no formato .txt e abrir no Vagas Generator.")

    def sobre(self):
        tkinter.messagebox.showinfo("Sobre o programa","Desenvolvido por Vinicius Pittigliani Perego para uso da equipe de TI da instituição São Marcos.")

    def onSave(self):
        if(self.textoEntrada==None):
           tkinter.messagebox.showinfo("Erro","Favor selecionar primeiro um arquivo de entrada.")
        else:
            arq_saida=tkinter.filedialog.asksaveasfile(mode='w',defaultextension='.txt')
            if self.modoSaida==True:
                self.saidaComVagas(self.textoEntrada,arq_saida)
            else:
                self.saidaSemVagas(self.textoEntrada,arq_saida)
            arq_saida.close()
        
    def saidaComVagas(self,texto,saida):
        palavras=self.tokens.word_tokenize(texto)
        titulos=["LOCAL","ÁREA","REQUISITOS","ATIVIDADES","REMUNERAÇÃO","HORÁRIO","BENEFÍCIO","CONTATO","DATAS","DATA"]
        principal="VAGAS"
        inicio=True
        aux=False
        doisPontos=False
        atuacaoAux=0
        dataAux=0
        for i in palavras:
            if aux==True:
                aux=False
                saida.write(" "+i+'\n<div class="vagas">')
            elif dataAux>0 and dataAux<=4:
                saida.write(i+" ")
                dataAux+=1
                if dataAux==4:
                    saida.write("</strong>")
            elif atuacaoAux>0 and atuacaoAux<=4:
                 saida.write(i+" ")
                 atuacaoAux+=1
                 if atuacaoAux==4:
                     saida.write("</strong>")
            elif doisPontos==True:
                 doisPontos=False
                 saida.write(i+"</strong>")
            else:
                 if i==principal and inicio==False:
                     aux=True
                     saida.write("</p>\n</div>\n"+i)
                 elif inicio==True:
                     inicio=False
                     aux=True
                     saida.write(i)
                 elif i=="LOCAL":
                    doisPontos=True
                    saida.write("\n<p><strong>"+i)
                 elif i in titulos:
                    if i =="ÁREA":
                        atuacaoAux=1
                        saida.write("</p> \n<p><strong>"+i+" ")
                    elif i=="DATAS":
                        dataAux=1
                        saida.write("</p> \n<p><strong>"+i+" ")
                    else:
                        doisPontos=True
                        saida.write("</p> \n<p><strong>"+i)
                 else:
                    saida.write(i+" ")
        saida.write("</p>\n</div>")

    def saidaSemVagas(self,texto,saida):
        palavras=self.tokens.word_tokenize(texto)
        titulos=["LOCAL","ÁREA","REQUISITOS","ATIVIDADES","REMUNERAÇÃO","HORÁRIO","BENEFÍCIO","CONTATO","DATAS","DATA"]
        principal="VAGAS"
        inicio=True
        aux=False
        doisPontos=False
        atuacaoAux=0
        dataAux=0
        for i in palavras:
            if aux==True:
                aux=False
                saida.write('\n<div class="vagas">')
            elif dataAux>0 and dataAux<=4:
                saida.write(i+" ")
                dataAux+=1
                if dataAux==4:
                   saida.write("</strong>")
            elif atuacaoAux>0 and atuacaoAux<=4:
                saida.write(i+" ")
                atuacaoAux+=1
                if atuacaoAux==4:
                   saida.write("</strong>")
            elif doisPontos==True:
                doisPontos=False
                saida.write(i+"</strong>")
            else:
                if i==principal and inicio==False:
                    aux=True
                    saida.write("</p>\n</div>\n")
                elif inicio==True:
                    inicio=False
                    aux=True
                elif i=="LOCAL":
                    doisPontos=True
                    saida.write("\n<p><strong>"+i)
                elif i in titulos:
                    if i =="ÁREA":
                        atuacaoAux=1
                        saida.write("</p> \n<p><strong>"+i+" ")
                    elif i=="DATAS":
                        dataAux=1
                        saida.write("</p> \n<p><strong>"+i+" ")
                    else:
                        doisPontos=True
                        saida.write("</p> \n<p><strong>"+i)
                else:
                    saida.write(i+" ")
        saida.write("</p>\n</div>")

    def onOpen(self):
        ftypes = [('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*')]
        dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        self.modoSaida=tkinter.messagebox.askyesno("Modo de leitura","Deseja colocar o tipo de vaga na saida?")
        if fl != '':
            text = self.readFile(fl)
            self.textoEntrada=text
            self.txt.insert(END,text)

    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def main():

    root = Tk()
    ex = Janela(root)
    root.geometry("300x250+300+300")
    center(root)
    root.mainloop()


if __name__ == '__main__':
    main()  
