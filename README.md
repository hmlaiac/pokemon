# pokemon
<h2>The purpose of this project is to analyze the battle data of pokemons. For example, sending some quiries to server and select the most suitable pokemon in battle.</h2>
<hr>

## Libraries to install
- requests
- BeautifulSoup
- re
- pandas

<h1>Extract Pokemon Data</h1>
<h2>9th GEN Resources are from Github</h2>
<a href="https://github.com/Ruimusume/PMSV">Please click here to check the recource link</a>
<h2>Data Crawler</h2>
<ol>
<li>Find all data from pokemon wiki</li>
<li><a href="https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%B8%95%E5%BA%95%E4%BA%9A%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89">Please Click here to check</a></li>
</ol>

<h1>Data Washing</h1>
<ol>
<li>Use Beautifulsoup to select some data</li>
<li>https://www.crummy.com/software/BeautifulSoup/bs4/doc/</li>
<li>Save selected data to database or pickle</li>
</ol>
<h1>Future Plan</h1>
<h2>Speed Analysis</h2>
<ul>
  <li>Simply sort speed of pokemon to check whehter it has advantage in battle</li>
  <li>Some pokemon may use items to increse the speed, show its statistics in different conditions e.g. 1.5x, 2x speed</li>
</ul>
<h2>Attack / SP_Attack Analysis</h2>
<ul>
  <li>To find a pokemon can one-turn kill other pokemons</li>
  <li>Users can adjust concentration of the pokemon. e.g. Best attack, good attck or normal attack</li>
</ul>

<h2>Defend Analysis</h2>
<ul>
  <li>Similar to attack analysis</li>
</ul>

<h1>Use reinforcement learning to select battle skills automatically</h1>
<h2>Build simulation project like OpenCV Gym</h2>
<h2>Build the battle AI</h2>



# Q1. How to select a skill figthing with other pokemon?
## Constraints
### 1. Limit 2 pokemons 
### 2. Limit 20 rounds to reduce computational workload
### 3. All skills of the pokemon are fixed (only 4)
### 4. Some debuffs are not allowed (e.g. poison, burn, shock ...)
## Observation
### 1. Current HP
### 2. Current Round
### 3. Oponent Pokemon name
### 4. Oponent Pokemon Type
### 5. Oponent Pokemon HP
## Action
#### SELECT one skill in battle
<s>Theory: Each pokemon can learn around 30-40 skills in the battle but only 4 skills are required. Of course, not all skills are useful in battle. We can pick 10 skills for a pokemon (Cont)</s>
