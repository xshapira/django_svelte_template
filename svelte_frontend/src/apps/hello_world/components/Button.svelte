<script>
    import { sendData } from '../../../shared/src/serverRequests.js';

    let textData = '';

    function sendTextInput() {
        sendData({ content: textData });
        textData = '';
    }
</script>

<input type="text" bind:value={textData}>
<button on:click={sendTextInput}>Send text to server</button>

<style>

</style>