# Procedural Byts

A fictional metal band whose albums cover the computer science curriculum, one decade and one genre at a time.

Each album covers one knowledge area from the ACM/IEEE-CS/AAAI **CS2023** curriculum. Every song teaches one concept, every solo acts it out, and every song comes with a ready-to-paste [Suno](https://suno.com) prompt.

**18 albums, 218 songs**, from *CS1* (1970, proto-metal) to *Superposition* (2024, the quantum reunion). [The making of](band/MAKING-OF.md) tells how it was built.

## The website

The static site lives in [`docs/`](docs/) and is ready for GitHub Pages:

1. Push this repository to GitHub.
2. In the repository settings, open **Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, then pick `main` and the `/docs` folder.

The site will be at `https://<your-username>.github.io/<repository-name>/`.

`docs/index.html` is the band home page: discography, members, trivia and curriculum coverage. Each album has a self-contained page in `docs/albums/` with lyrics, liner notes, lessons and copy buttons for every Suno prompt.

## What’s in here

| Path | Contents |
| --- | --- |
| `docs/` | The static website (GitHub Pages) |
| `data/band.json` | Members, trivia and upcoming albums |
| `data/albums/*.json` | Every album: description, story, lineup and songs, including lyrics, lessons and Suno prompts |
| `lyrics/` | One Markdown file per song: lyrics, the lesson, and the full Suno prompt |
| `band/` | The band history, members, trivia and the making of the project, as Markdown |
| `docs/archive/` | Early artifacts from the project, kept exactly as they were |

## Albums

| Year | Album | Genre | CS2023 knowledge area |
| --- | --- | --- | --- |
| 1970 | [CS1](lyrics/1970-cs1/README.md) | 1970s heavy metal | Software development fundamentals |
| 1973 | [Fetch, Decode, Execute](lyrics/1973-fetch-decode-execute/README.md) | 1973 heavy blues rock | Architecture and organization |
| 1976 | [Kernel Panic](lyrics/1976-kernel-panic/README.md) | 1976 hard rock with an early punk edge | Operating systems |
| 1979 | [Syntax Error](lyrics/1979-syntax-error/README.md) | 1979 new wave of British heavy metal | Foundations of programming languages |
| 1982 | [Packet Storm](lyrics/1982-packet-storm/README.md) | 1982 classic heavy metal | Networking and communication |
| 1985 | [CS2: Live on the Abstract Data Tour ’85](lyrics/1985-cs2-live/README.md) | 1985 heavy metal | Algorithmic foundations |
| 1989 | [Q.E.D.](lyrics/1989-qed/README.md) | 1989 progressive metal concept album | Mathematical and statistical foundations |
| 1992 | [Third Normal Form](lyrics/1992-third-normal-form/README.md) | 1992 grunge and alternative metal | Data management |
| 1995 | [Merge Conflict](lyrics/1995-merge-conflict/README.md) | 1995 industrial metal | Software engineering |
| 1998 | [Buffer Overflow](lyrics/1998-buffer-overflow/README.md) | 1998 industrial metal with techno crossover | Security |
| 2001 | [Race Condition](lyrics/2001-race-condition/README.md) | 2001 nu-metal | Parallel and distributed computing |
| 2004 | [Rasterize](lyrics/2004-rasterize/README.md) | 2004 metalcore | Graphics and interactive techniques |
| 2007 | [User Error](lyrics/2007-user-error/README.md) | 2007 alternative metal | Human-computer interaction |
| 2010 | [Cross-Platform](lyrics/2010-cross-platform/README.md) | 2010 electronic rock | Specialized platform development |
| 2013 | [Cache Me If You Can](lyrics/2013-cache-me-if-you-can/README.md) | 2013 djent progressive metal | Systems fundamentals |
| 2016 | [Terms of Service](lyrics/2016-terms-of-service/README.md) | 2016 post-metal | Society, ethics, and professionalism |
| 2019 | [Gradient Descent](lyrics/2019-gradient-descent/README.md) | 2019 synthwave metal | Artificial intelligence |
| 2024 | [Superposition](lyrics/2024-superposition/README.md) | genre-blending metal | Bonus: quantum computing |


## License

The code that builds the site is under the MIT License (see `LICENSE`). The lyrics, stories and other written content are under Creative Commons Attribution 4.0 (see `LICENSE-CONTENT`). Audio you generate with Suno from these prompts is governed by Suno’s own terms.
