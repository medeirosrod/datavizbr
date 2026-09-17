import rss from '@astrojs/rss';
import { SITE } from '../consts';
import { getPostsParaFeed } from '../lib/data';

export async function GET(context) {
	const posts = await getPostsParaFeed();
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
