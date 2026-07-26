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

    <h1>Startup Name Generator</h1>

    <p>Industry</p>
    <input
        v-model="industry"
        placeholder="ex) Technology"
    />

    <br><br>

    <p>Keyword</p>
    <input
        v-model="keyword"
        placeholder="ex) AI"
    />

    <br><br>

    <button
        @click="generate"
        :disabled="loading"
    >

        {{ loading ? "Generating..." : "Generate"}}

    </button>

    <p v-if="errorMessage">
        {{ errorMessage }}
    </p>

    <p v-if="loading">
        Generating...
    </p>

    <p v-if="!results.length && !loading">
        Let's generate your startup name!
    </p>
    <div v-if="results.length">

        <h2>Results</h2>

        <ul>
            <li
                v-for="result in results"
                :key="result"
            >

                {{ result }}

                <button
                    @click="copyName(result)"
                >

                {{ copiedText === result
                ? "Copied!"
                : "Copy"
                }}

                </button>

            </li>
        </ul>

    </div>

</template>