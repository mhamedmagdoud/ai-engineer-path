from dotenv import load_dotenv
import anthropic

load_dotenv()  # lit .env et place ANTHROPIC_API_KEY dans les variables d'environnement

client = anthropic.Anthropic()  # récupère la clé automatiquement depuis l'environnement


def ask_claude(messages: list[dict]) -> tuple[str, int]:

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=messages,
    )

    print(
        f"Tokens — entrée : {response.usage.input_tokens}, sortie : {response.usage.output_tokens}"
    )

    text = response.content[0].text
    tokens = response.usage.input_tokens + response.usage.output_tokens
    return text, tokens


def main() -> None:
    messages = []
    total_tokens = 0
    while True:
        text = input("> ")
        if text == "exit":
            break
        messages.append({"role": "user", "content": text})
        answer, usage = ask_claude(messages)
        messages.append({"role": "assistant", "content": answer})
        print(answer)
        total_tokens += usage
        print(total_tokens)


if __name__ == "__main__":
    main()
