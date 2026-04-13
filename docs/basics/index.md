# Basics

Core concepts and components to build, solve, and inspect models in Llama.

<div class="category-grid">

<a class="category-card" href="analysis/">
  <div class="category-card__title">Analysis</div>
  <div class="category-card__desc">The **Build Input Deck** component writes the assembled model to a CalculiX `.inp` file.</div>
</a>

<a class="category-card" href="assemble/">
  <div class="category-card__title">Assemble Model</div>
  <div class="category-card__desc">The **CcxModel** component assembles all parts of the structural model into a single CalculiX model ready for analysis.</div>
</a>

<a class="category-card" href="boundary-conditions/">
  <div class="category-card__title">Boundary Conditions</div>
  <div class="category-card__desc">The **Support** component applies fixed boundary conditions to selected nodes, constraining all translational and rot...</div>
</a>

<a class="category-card" href="elements/">
  <div class="category-card__title">Elements</div>
  <div class="category-card__desc">!welcome{.invert-in-dark}</div>
</a>

<a class="category-card" href="loads/">
  <div class="category-card__title">Loads</div>
  <div class="category-card__desc">Applies a gravitational body force to the entire model.</div>
</a>

<a class="category-card" href="materials/">
  <div class="category-card__title">Materials</div>
  <div class="category-card__desc">Llama supports several material models for use with CalculiX.</div>
</a>

<a class="category-card" href="meshing/">
  <div class="category-card__title">Meshing</div>
  <div class="category-card__desc">Llama integrates Gmsh for tetrahedral mesh generation.</div>
</a>

<a class="category-card" href="results/">
  <div class="category-card__title">Results</div>
  <div class="category-card__desc">The **Read Results** component parses CalculiX output files (`.dat`, `.frd`) and extracts analysis results.</div>
</a>

<a class="category-card" href="steps/">
  <div class="category-card__title">Analysis Steps</div>
  <div class="category-card__desc">Steps define the type of analysis to perform.</div>
</a>

</div>
