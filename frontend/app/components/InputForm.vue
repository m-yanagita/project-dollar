<script setup>

const industry = defineModel("industry")
const keyword = defineModel("keyword")

</script>


<template>

<div>

<p>
Industry
</p>

<input
v-model="industry"
placeholder="Technology"
/>


<p>
Keyword
</p>

<input
v-model="keyword"
placeholder="AI Future"
/>

</div>

</template>