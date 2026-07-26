<script setup>
import { ref } from "vue"

const industry = ref("")
const keyword = ref("")
const results = ref([])
const errorMessage = ref("")
const loading = ref(false)
const copiedText = ref("")

const copyName = async(name)=>{

    await navigator.clipboard.writeText(
        name
    )

    copiedText.value = name

    setTimeout(()=>{

        copiedText.value = ""

    },2000)

}

const generate = async () => {

    results.value = []

    if (!industry.value && !keyword.value) {

        errorMessage.value =
            "Please enter Industry and Keyword."

        return

    }

    if (!industry.value) {

        errorMessage.value =
            "Please enter Industry."

        return

    }

    if (!keyword.value) {

        errorMessage.value =
            "Please enter Keyword."

        return

    }

    //エラー文を消す
    try {

        errorMessage.value = ""

        loading.value = true

        const response = await $fetch(
            "http://127.0.0.1:8000/name-generator",
            {
                method: "POST",
                body: {
                    industry: industry.value,
                    keyword: keyword.value
                }
            }
        )

        results.value = response.results

    } catch (error) {

        errorMessage.value =
            "Something went wrong."

    } finally {

        loading.value = false

    }

}

</script>

<template>

<div class="container">

    <h1 class="title">
        Project Dollar
    </h1>

    <p class="sub-title">

        Build Tools For Entrepreneurs

    </p>


<div class="card">

<h2>

    Startup Name Generator

</h2>

<br>

<p class="input-label">Industry</p>
<input

class="input-box"

v-model="industry"

placeholder="ex) Technology"

/>

<p class="input-label">Keyword</p>
<input

class="input-box"

v-model="keyword"

placeholder="ex) AI"

/>


<button

class="button"

@click="generate"

:disabled="loading"

>

{{loading ? "Generating..." : "Generate"}}

</button>

<br><br>

<p v-if="errorMessage">

{{errorMessage}}

</p>

</div>


<br>


<p
v-if="!results.length && !loading"
>

Let's generate your startup name!


</p>


<div
v-for="result in results"
:key="result"

class="result-card"

>

<h3>

{{result}}

</h3>


<button

class="copy-button"

@click="copyName(result)"

>

{{ copiedText === result
? "Copied!"
: "Copy"

}}

</button>


</div>


</div>

</template>

<style scoped>

.container{
    max-width:800px;
    margin:50px auto;
    padding:30px;
}


.title{
    text-align:center;
    font-size:50px;
}


.sub-title{

    text-align:center;
    color:gray;
    margin-bottom:50px;

}

.input-label{

    font-weight:bold;
    margin-bottom:5px;
    display:block;

}

.card{

    background:white;
    padding:40px;
    border-radius:20px;
    box-shadow:0 0 20px rgba(0,0,0,.1);

}


.input-box{

    width:100%;
    padding:15px;
    border-radius:10px;
    border:1px solid #ccc;
    margin-bottom:20px;
    box-sizing:border-box;

}


.button{

    width:100%;
    padding:15px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    font-size:18px;
    background:black;
    color:white;

}


.result-card{

    display:flex;
    justify-content:space-between;
    align-items:center;

    padding:20px;
    margin-top:15px;

    border-radius:10px;

    box-shadow:0 0 10px rgba(0,0,0,.08);

}


.copy-button{

    padding:10px 20px;
    cursor:pointer;
    border:none;
    border-radius:10px;
    background:#f4f4f4;

}

</style>