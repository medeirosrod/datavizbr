import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';
import { SITE } from '../consts';

export async function GET(context) {
	const posts = await getCollection('posts', ({ data }) => !data.rascunho && !data.arquivo);
	return rss({
		title: SITE.nome,
		description: SITE.descricao,
		site: context.site,
		items: posts.map((post) => ({
			...post.data,
			link: `/posts/${post.id}/`,
		})),
	});
}
