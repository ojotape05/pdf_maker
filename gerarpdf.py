# PyMuPDF
import fitz, os

def open_pdf(file_path):

    try:
        os.startfile(file_path)
        print(f"Arquivo {file_path} aberto com o programa padrão.")
    except Exception as e:
        print(f"Falha para abrir o arquivo: {e}")


def gerar_pdf():

    # Caminho para o arquivo PDF de entrada
    input_file_path = 'template.pdf'
    # Caminho para o arquivo PDF de saída
    output_file_path = 'output.pdf'

    # Abrir o documento PDF
    pdf_document = fitz.open(input_file_path)

    infos = {
        "${id}": "#01",
        "${mutuario}": "Isabela Bermudes da Silva Silvestre",
        "${contrato}": "0201.00000.000-1",
        "${data_comando}": "R$ 17/05/2024",
        "${dt_envio}": "R$ 17/05/2024",
        "${valor_financiado}": "1.600.000,00",
        "${valor_financiado_corrigido}": "1.600.000,00",
        "${valor_fgts}": "1.600.000,00",
        "${valor_fgts_corrigido}": "1.600.000,00",
        "${valor_iq}": "1.600.000,00",
        "${dt_iq}": "17/05/2024",
        "${correspondente}": "N SEI OQ LTDA",
        "${agencia}": "777",
        "${valor_ted}": "1.600.000,00",
        "${valor_custas}": "1.600.000,0"
    }

    page = pdf_document.load_page(0)

    for text_search in infos.keys():

        text_instances = page.search_for(text_search)

        new_text = infos[text_search]
        #print(text_search,new_text)

        if text_search in ["${id}","${mutuario}", "${contrato}", "${dt_envio}"]:

            for inst in text_instances:
                rect = inst

                #Apagar o texto antigo
                page.add_redact_annot(rect, fill=(1, 1, 1))
                page.apply_redactions()

                center_x = (rect.x0 + rect.x1) / 2
                center_y = (rect.y0 + rect.y1) / 2

                font_size = 8.5
                new_text_width = font_size * 0.5 * len(new_text)  # Aproximação da largura do texto
                new_text_height = font_size  # Altura do texto

                insert_x = (center_x - new_text_width / 2) 
                insert_y = (center_y + new_text_height / 4) 

                page.insert_text(
                    (insert_x, insert_y),  # Posição do texto centralizado
                    new_text,  # Novo texto
                    fontsize=font_size,  # Tamanho da fonte
                    fontname="helv",  # Nome da fonte
                    color=(0, 0, 0),  # Cor do texto (preto)
                    overlay=True  # Sobrepor texto ao invés de substituir
                )
        
        elif "valor" in text_search or text_search == "${dt_iq}":

            # Percorrer todas as instâncias do texto encontrado
            for inst in text_instances:
                # Apagar o texto antigo
                page.add_redact_annot(inst, fill=(1, 1, 1))
                page.apply_redactions()

                coord_x = inst.x0
                coord_y = inst.y1 - 2

                # Adicionar o novo texto
                page.insert_text(
                    (coord_x, coord_y),  # Posição do texto centralizado
                    new_text,  # Novo texto
                    fontsize=10,  # Tamanho da fonte
                    fontname="helv",  # Nome da fonte
                    color=(0, 0, 0),  # Cor do texto (em formato RGB)
                    overlay=True  # Sobrepor texto ao invés de substituir
                )

        elif text_search in ['${agencia}', '${correspondente}']:

            if text_search == '${correspondente}':
                fontsize = 6
            else:
                fontsize = 10
            
            # Percorrer todas as instâncias do texto encontrado
            for inst in text_instances:
                # Apagar o texto antigo
                page.add_redact_annot(inst, fill=(1, 1, 1))
                page.apply_redactions()

                coord_x = inst.x0
                coord_y = inst.y1 - 2.5

                # Adicionar o novo texto
                page.insert_text(
                    (coord_x, coord_y),  # Posição do texto centralizado
                    new_text,  # Novo texto
                    fontsize=fontsize,  # Tamanho da fonte
                    fontname="helv",  # Nome da fonte
                    color=(0, 0, 0),  # Cor do texto (em formato RGB)
                    overlay=True  # Sobrepor texto ao invés de substituir
                )
        
        else:
            # Percorrer todas as instâncias do texto encontrado
            for inst in text_instances:
                # Apagar o texto antigo
                page.add_redact_annot(inst, fill=(1, 1, 1))
                page.apply_redactions()

                page.insert_text(
                    point=(inst.x0,inst.y1),
                    text=new_text,  # Novo texto
                    fontsize=11,  # Tamanho da fonte
                    fontname="helv",  # Nome da fonte
                    color=(0, 0, 0),  # Cor do texto (preto)
                    overlay=True  # Sobrepor texto ao invés de substituir
                )

    # Salvar o documento atualizado
    pdf_document.save(output_file_path)
    open_pdf(output_file_path)
    #print_pdf(output_file_path)

    print("Impressão realizada!")
    #os.remove(output_file_path)

gerar_pdf()
