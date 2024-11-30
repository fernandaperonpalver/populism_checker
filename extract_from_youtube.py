import pandas as pd
from youtube_transcript_api import TranscriptsDisabled, YouTubeTranscriptApi

# ID do vídeo do YouTube

df_populism = pd.read_excel("base_principal.xlsx")

# df_populism = pd.read_excel("bocalom_teste.xlsx")
df_populism["transcricao"] = None


for i, row in df_populism.iterrows():
    link = row["Link sabatina candidato"]

    if pd.notnull(link) and "youtube.com" in link:
        try:
            video_id = link.split("v=")[-1].split("&")[0]

            transcript = None
            try:
                transcript = YouTubeTranscriptApi.get_transcript(
                    video_id, languages=["pt"]
                )
            except:
                # Tentar buscar em qualquer idioma disponível como fallback
                transcript = YouTubeTranscriptApi.get_transcript(video_id)

            # Combinar as transcrições em um único texto
            transcricao = " ".join([entry["text"] for entry in transcript])

            # Adicionar a transcrição ao DataFrame
            df_populism.at[i, "transcricao"] = transcricao

        except TranscriptsDisabled:
            df_populism.at[i, "transcricao"] = (
                "Transcrições desativadas para este vídeo."
            )
        except NoTranscript:
            df_populism.at[i, "transcricao"] = (
                "Nenhuma transcrição disponível para este vídeo."
            )
        except Exception as e:
            df_populism.at[i, "transcricao"] = f"Erro: {e}"

# df_populism.to_excel("base_principal_com_transcricoes.xlsx", index=False)
