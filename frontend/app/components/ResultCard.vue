<script setup>

defineProps({
    results:{
        type:Array,
        required:true
    }
})

</script>


<template>

<div>

<h2>
Results
</h2>


<ul>

<li
v-for="result in results"
:key="result"
>

✨ {{ result }}

</li>

</ul>

</div>

</template>