<template>
  <div>
    <{{cookiecutter.component}} title="{{cookiecutter.component}}" content="This page is under construction" />
  </div>
</template>

<script>
import {{cookiecutter.component | title | replace('-','')}} from './../web-components/{{cookiecutter.component}}.vue';


export default {
  name: 'MyView',
  components: {
    {{cookiecutter.component | title | replace('-','')}},
  },
};
</script>

<style>
</style>
