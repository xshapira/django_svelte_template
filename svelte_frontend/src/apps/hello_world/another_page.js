import App from './components/App.svelte';

const app = new App({
	target: document.body,
	props: {
		name: ', I am another page'
	}
});

export default app;