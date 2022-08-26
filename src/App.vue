<template>
  <v-app class="mainFontRegular">
    <v-container>
      <p>PokedexApp</p>
    </v-container>
    <v-container>
      <v-card
        class="mx-auto"
        color="#8bbe8a"
        v-for="pokemon in pokemons"
        max-height="150px"
        :key="pokemon.id"
      >
        <v-row no-gutters>
          <v-col>
            <v-container fluid>
              <v-card-text
                class="mainFontBold"
              >#{{pokemon.id}}</v-card-text>
              <v-card-text
                class="nameFont mt-n6 white--text"
              >{{pokemon.name}}</v-card-text>
              <v-col>
                <v-row class="ml-n6 mt-n8">
                  <v-card
                    :color="type.color"
                    v-for="type in pokemon.types"
                    :key="type.id"
                    max-width="90px"
                    height="35px"
                    class="mr-n4"
                  >
                  <v-col>
                    <v-row>
                      <v-img
                        src="./assets/Vector.svg"
                        max-width="20px"
                        height="20px"
                      ></v-img>
                    </v-row>
                    <v-row>
                      <v-card-text
                        class="mt-n6 mr-4 white--text caption"
                      >{{type.name}}</v-card-text>
                    </v-row>
                  </v-col>
                  </v-card>
                </v-row>
              </v-col>
            </v-container>
          </v-col>
          <v-col>
            <v-container>
              <v-img
                width="130px"
                :src="pokemon.images.svgs.front_default"  
              ></v-img>
            </v-container>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
    pokemons: []
  }),
  created() {
    this.getPokemons();
  },
  methods: {
    async getPokemons () {
      try {
        let response = await axios.get('/pokemons')
        this.pokemons = response.data.data;
        console.log(this.pokemons.data.images.svgs.front_default);
      } catch (error) {
        console.log(error);
      }
    }
  }
};
</script>

<style scoped>
  .v-card {
    margin: 25px;
  }
  .mainFontRegular {
    font-family: "SFPro";
    src: local("SFPro"),
    url(./assets/fonts/SFPRODISPLAYREGULAR.OTF) format("truetype");
  }
  .mainFontBold {
    font-family: "SFPro";
    src: local("SFPro"),
    url(./assets/fonts/SFPRODISPLAYREGULAR.OTF) format("truetype");
    font-weight: bold;
  }
  .nameFont {
    color: red;
    font-size: 2rem;
  }
</style>
