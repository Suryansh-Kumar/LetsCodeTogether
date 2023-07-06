from flask import Flask, render_template

app = Flask(__name__)

SKILLS = [["python", "Python"], ["html", "HTML"], ["css", "CSS"], [
    "js", "JS"], ["bootstrap", "Bootstrap"], ["tailwind", "Tailwind CSS"]]


@app.route("/")
def home():
    html_code = """
   <div hidden id="card-container-html">
        <div class="language">
          <h2>HTML</h2>
          <img class="html-img" src="static/img/html-logo.png" alt="" />
        </div>
        <p class="desc">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum illo
          dolor necessitatibus perferendis. Ea ipsum iusto laboriosam
          voluptates? Sunt, ex exercitationem sit quae animi suscipit atque
          cumque doloribus nam quisquam.
        </p>
        <div class="buttons">
          <a
            class="documentation"
            href=" https://developer.mozilla.org/en-US/docs/Web/HTML"
            ><button class="btn btn-1">Documentation</button>
          </a>
          <a href="/">
            <button disabled class="btn btn-2">My Projects</button>
          </a>
        </div>
      </div>
      <div hidden id="card-container-python">
        <div class="language">
          <h2>Python</h2>
          <img class="html-img" src="static/img/python.jpg" alt="" />
        </div>
        <p class="desc">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum illo
          dolor necessitatibus perferendis. Ea ipsum iusto laboriosam
          voluptates? Sunt, ex exercitationem sit quae animi suscipit atque
          cumque doloribus nam quisquam.
        </p>
        <div class="buttons">
          <a class="documentation" href="https://docs.python.org/3/"
            ><button class="btn btn-1">Documentation</button>
          </a>
          <a href="/">
            <button disabled class="btn btn-2">My Projects</button>
          </a>
        </div>
      </div>
      <div hidden id="card-container-css">
        <div class="language">
          <h2>CSS</h2>
          <img class="html-img" src="static/img/css-logo.jpg" alt="" />
        </div>
        <p class="desc">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum illo
          dolor necessitatibus perferendis. Ea ipsum iusto laboriosam
          voluptates? Sunt, ex exercitationem sit quae animi suscipit atque
          cumque doloribus nam quisquam.
        </p>
        <div class="buttons">
          <a
            class="documentation"
            href="https://developer.mozilla.org/en-US/docs/Web/CSS"
            ><button class="btn btn-1">Documentation</button>
          </a>
          <a href="/">
            <button disabled class="btn btn-2">My Projects</button>
          </a>
        </div>
      </div>
      <div hidden id="card-container-js">
        <div class="language">
          <h2>JavaScript</h2>
          <img class="html-img" src="static/img/js-logo.jpg" alt="" />
        </div>
        <p class="desc">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum illo
          dolor necessitatibus perferendis. Ea ipsum iusto laboriosam
          voluptates? Sunt, ex exercitationem sit quae animi suscipit atque
          cumque doloribus nam quisquam.
        </p>
        <div class="buttons">
          <a
            class="documentation"
            href=" https://developer.mozilla.org/en-US/docs/Web/JavaScript"
            ><button class="btn btn-1">Documentation</button>
          </a>
          <a href="/">
            <button disabled class="btn btn-2">My Projects</button>
          </a>
        </div>
      </div>
      <div hidden id="card-container-tailwind">
        <div class="language">
          <h2>Tailwind CSS</h2>
          <img class="html-img" src="static/img/tailwindcss.png" alt="" />
        </div>
        <p class="desc">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum illo
          dolor necessitatibus perferendis. Ea ipsum iusto laboriosam
          voluptates? Sunt, ex exercitationem sit quae animi suscipit atque
          cumque doloribus nam quisquam.
        </p>
        <div class="buttons">
          <a class="documentation" href="https://tailwindcss.com/"
            ><button class="btn btn-1">Documentation</button>
          </a>
          <a href="/">
            <button disabled class="btn btn-2">My Projects</button>
          </a>
        </div>
      </div>
      <div hidden id="card-container-bootstrap">
        <div class="language">
          <h2>Bootstrap</h2>
          <img class="html-img" src="static/img/bootstrap-logo.png" alt="" />
        </div>
        <p class="desc">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum illo
          dolor necessitatibus perferendis. Ea ipsum iusto laboriosam
          voluptates? Sunt, ex exercitationem sit quae animi suscipit atque
          cumque doloribus nam quisquam.
        </p>
        <div class="buttons">
          <a class="documentation" href="https://getbootstrap.com/"
            ><button class="btn btn-1">Documentation</button>
          </a>
          <a href="/">
            <button disabled class="btn btn-2">My Projects</button>
          </a>
        </div>
      </div>
    """
    project_card_content = {
        "card1": {
            "image_url": "/static/img/portfolio.png",
            "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti excepturi consequuntur pariatur repellendus a et quasi optio voluptatum quaerat, vero, nam eligendi. Hic, numquam atque itaque necessitatibus autem reiciendis maiores quidem doloribus quisquam quaerat provident soluta vero expedita totam ipsum."
        },
        "card2":  {
            "image_url": "/static/img/portfolio.png",
            "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti excepturi consequuntur pariatur repellendus a et quasi optio voluptatum quaerat, vero, nam eligendi. Hic, numquam atque itaque necessitatibus autem reiciendis maiores quidem doloribus quisquam quaerat provident soluta vero expedita totam ipsum."
        },
        "card3":  {
            "image_url": "/static/img/portfolio.png",
            "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti excepturi consequuntur pariatur repellendus a et quasi optio voluptatum quaerat, vero, nam eligendi. Hic, numquam atque itaque necessitatibus autem reiciendis maiores quidem doloribus quisquam quaerat provident soluta vero expedita totam ipsum."
        },
    }
    return render_template("index.html", skills=SKILLS, html=html_code, name="LetsCodeTogether", pcc=project_card_content)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

