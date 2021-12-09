Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        Import(
            names=[alias(name='inspect', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[
                alias(name='etree', asname=None),
                alias(name='html', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='sql', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.datastructures',
            names=[alias(name='OrderedMultiDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='NotFound', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
                alias(name='http', asname=None),
                alias(name='release', asname=None),
                alias(name='registry', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[
                alias(name='slugify', asname=None),
                alias(name='_guess_mimetype', asname=None),
                alias(name='url_for', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.models.ir_http',
            names=[alias(name='sitemap_qs2dom', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.tools',
            names=[
                alias(name='get_unaccent_sql_wrapper', asname=None),
                alias(name='similarity_score', asname=None),
                alias(name='text_from_html', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers.portal',
            names=[alias(name='pager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.iap.tools',
            names=[alias(name='iap_tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='AccessError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_resource_path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[
                alias(name='AND', asname=None),
                alias(name='OR', asname=None),
                alias(name='FALSE_DOMAIN', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='escape_psql', asname=None),
                alias(name='pycompat', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_CDN_FILTERS', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='^/[^/]+/static/', kind=None),
                    Constant(value='^/web/(css|js)/', kind=None),
                    Constant(value='^/web/image', kind=None),
                    Constant(value='^/web/content', kind=None),
                    Constant(value='^/web/assets', kind=None),
                    Constant(value='^/website/image/', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_ENDPOINT', ctx=Store())],
            value=Constant(value='https://website.api.odoo.com', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='Website',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='website', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Website', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence, id', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='website_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='website_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='website_id', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_active_languages',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.lang', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_language',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lang_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.default', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='lang', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='def_lang_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_lang_get_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='lang_code', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='def_lang_id', ctx=Load()),
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_active_languages',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Website Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='domain', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Website Domain', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='E.g. https://www.mydomain.com', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='country_group_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.country.group', kind=None),
                            Constant(value='website_country_group_rel', kind=None),
                            Constant(value='website_id', kind=None),
                            Constant(value='country_group_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Country Groups', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Used when multiple websites have the same domain.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='language_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.lang', kind=None),
                            Constant(value='website_lang_rel', kind=None),
                            Constant(value='website_id', kind=None),
                            Constant(value='lang_id', kind=None),
                            Constant(value='Languages', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='_active_languages', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='default_lang_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.lang', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Default Language', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='_default_language', ctx=Load()),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='auto_redirect_lang', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Autoredirect Language', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Should users be redirected to their browser's language", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cookies_bar', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Cookies Bar', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Display a customizable cookies bar on your website.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='configurator_done', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='True if configurator has been completed or ignored', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_social_facebook',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.main_company', kind=None)],
                                    keywords=[],
                                ),
                                attr='social_facebook',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_social_github',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.main_company', kind=None)],
                                    keywords=[],
                                ),
                                attr='social_github',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_social_linkedin',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.main_company', kind=None)],
                                    keywords=[],
                                ),
                                attr='social_linkedin',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_social_youtube',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.main_company', kind=None)],
                                    keywords=[],
                                ),
                                attr='social_youtube',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_social_instagram',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.main_company', kind=None)],
                                    keywords=[],
                                ),
                                attr='social_instagram',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_social_twitter',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.main_company', kind=None)],
                                    keywords=[],
                                ),
                                attr='social_twitter',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_logo',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='image_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_resource_path', ctx=Load()),
                                args=[
                                    Constant(value='website', kind=None),
                                    Constant(value='static/src/img', kind=None),
                                    Constant(value='website_logo.svg', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='file_open',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='image_path', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='f', ctx=Store()),
                                ),
                            ],
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='logo', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Website Logo', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='_default_logo', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Display this logo on the website.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='social_twitter', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Twitter Account', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='_default_social_twitter', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='social_facebook', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Facebook Account', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='_default_social_facebook', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='social_github', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='GitHub Account', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='_default_social_github', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='social_linkedin', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='LinkedIn Account', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='_default_social_linkedin', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='social_youtube', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Youtube Account', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='_default_social_youtube', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='social_instagram', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Instagram Account', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='_default_social_instagram', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='social_default_image', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Default Social Share Image', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If set, replaces the website logo as the default social share image.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='has_social_default_image', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_has_social_default_image', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='google_analytics_key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Google Analytics Key', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='google_management_client_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Google Client ID', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='google_management_client_secret', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Google Client Secret', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='google_search_console', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Google key, or Enable to access first reply', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='google_maps_api_key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Google Maps API Key', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Public User', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cdn_activated', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Content Delivery Network (CDN)', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cdn_url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='CDN Base URL', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cdn_filters', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='CDN Filters', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='s', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        func=Attribute(
                                            value=Constant(value='\n', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='DEFAULT_CDN_FILTERS', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='URL matching those filters will be rewritten using the CDN Base URL', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='user_id.partner_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Public Partner', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='menu_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='website.menu', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_menu', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Main Menu', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='homepage_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='website.page', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Homepage', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='custom_code_head', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Custom <head> code', kind=None)],
                        keywords=[
                            keyword(
                                arg='sanitize',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='custom_code_footer', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Custom end of <body> code', kind=None)],
                        keywords=[
                            keyword(
                                arg='sanitize',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='robots_txt', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Robots.txt', kind=None)],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='website.group_website_designer', kind=None),
                            ),
                            keyword(
                                arg='sanitize',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_favicon',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='img_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_resource_path', ctx=Load()),
                                args=[
                                    Constant(value='web', kind=None),
                                    Constant(value='static/img/favicon.ico', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='file_open',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='img_path', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='f', ctx=Store()),
                                ),
                            ],
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='favicon', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Website Favicon', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field holds the image used to display a favicon on the website.', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='_default_favicon', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='theme_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.module.module', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Installed theme', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='specific_user_account', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Specific User Account', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='If True, new accounts will be associated to the current website', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='auth_signup_uninvited', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='b2b', kind=None),
                                            Constant(value='On invitation', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='b2c', kind=None),
                                            Constant(value='Free sign up', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Customer Account', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='b2b', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_language_ids',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='language_ids', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='language_ids',
                                    ctx=Load(),
                                ),
                                attr='_origin',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='language_ids', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='default_lang_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='language_ids', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='default_lang_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='language_ids', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='language_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_has_social_default_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='website', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='website', ctx=Load()),
                                            attr='has_social_default_image',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='website', ctx=Load()),
                                                attr='social_default_image',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='social_default_image', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_menu',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='website', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='menus', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.menu', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='_get_menu_ids',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='menu', ctx=Store()),
                                    iter=Name(id='menus', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='menu', ctx=Load()),
                                                        attr='_cache',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='child_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='menu', ctx=Store()),
                                    iter=Name(id='menus', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='menu', ctx=Load()),
                                                        attr='parent_id',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='menu', ctx=Load()),
                                                            attr='parent_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='menus', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='menu', ctx=Load()),
                                                                attr='parent_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_cache',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='child_id', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='menu', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='menus', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='is_visible', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='top_menus', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='menus', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='parent_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='website', ctx=Load()),
                                            attr='menu_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='top_menus', ctx=Load()),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='top_menus', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_menu_ids',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='website.menu', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='website_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='self.env.uid', kind=None),
                                Constant(value='self.id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_create_write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='user_id', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='vals', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='company_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='user_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Name(id='company', ctx=Load()),
                                        body=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='_get_public_user',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='base.public_user', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Website', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='res', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_website_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='_bootstrap_homepage',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='website.group_multi_website', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='search_count',
                                                ctx=Load(),
                                            ),
                                            args=[List(elts=[], ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='all_user_groups', ctx=Store())],
                                    value=Constant(value='base.group_portal,base.group_user,base.group_public', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='groups', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.groups', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='concat',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=GeneratorExp(
                                                    elt=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='it', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='it', ctx=Store()),
                                                            iter=Call(
                                                                func=Attribute(
                                                                    value=Name(id='all_user_groups', ctx=Load()),
                                                                    attr='split',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=',', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='groups', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='implied_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=4, kind=None),
                                                                    Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='ref',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='website.group_multi_website', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='public_user_to_change_websites', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='website', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='original_company', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_create_write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='company_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='user_id', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='public_user_to_change_websites', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='w', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='w', ctx=Load()),
                                                                        attr='sudo',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                attr='user_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='company_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='public_user_to_change_websites', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='company', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.company', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='company_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='super', ctx=Load()),
                                                        args=[
                                                            Name(id='Website', ctx=Load()),
                                                            Name(id='public_user_to_change_websites', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[Name(id='values', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='user_id',
                                                                value=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Name(id='company', ctx=Load()),
                                                                        Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='company', ctx=Load()),
                                                                                    attr='_get_public_user',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Website', ctx=Load()),
                                            BinOp(
                                                left=Name(id='self', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='public_user_to_change_websites', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='cdn_activated', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='cdn_url', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='cdn_filters', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='clear_caches',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='sequence', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='company_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='original_company', ctx=Load()),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='_compute_website_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='cookies_bar', kind=None),
                                ops=[In()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='existing_policy_page', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.page', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='website_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='url', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='/cookie-policy', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='cookies_bar', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='existing_policy_page', ctx=Load()),
                                                    attr='unlink',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='existing_policy_page', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='cookies_view', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='website.cookie_policy', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='raise_if_not_found',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='cookies_view', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='cookies_view', ctx=Load()),
                                                                            attr='with_context',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='website_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[Constant(value='website_id', kind=None)],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='specific_cook_view', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='with_context',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='website_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    attr='viewref',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='website.cookie_policy', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='website.page', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='is_published', kind=None),
                                                                            Constant(value='website_indexed', kind=None),
                                                                            Constant(value='url', kind=None),
                                                                            Constant(value='website_id', kind=None),
                                                                            Constant(value='view_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value='/cookie-policy', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='specific_cook_view', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_create_write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_favicon',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_domain',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_favicon',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='favicon', kind=None),
                                ops=[In()],
                                comparators=[Name(id='vals', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='favicon', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='favicon', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='size',
                                                value=Tuple(
                                                    elts=[
                                                        Constant(value=256, kind=None),
                                                        Constant(value=256, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='crop',
                                                value=Constant(value='center', kind=None),
                                            ),
                                            keyword(
                                                arg='output_format',
                                                value=Constant(value='ICO', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='domain', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Subscript(
                                        value=Name(id='vals', ctx=Load()),
                                        slice=Constant(value='domain', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='domain', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='http', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='domain', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value='https://%s', kind=None),
                                                op=Mod(),
                                                right=Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='domain', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='domain', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='domain', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='rstrip',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_unlink_except_last_remaining_website',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='not in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='website', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You must keep at least one website.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='ondelete',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='at_uninstall',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='attachments_to_unlink', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='key', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Constant(value='.custom.', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Constant(value='.assets\\_', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attachments_to_unlink', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='companies', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Website', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='companies', ctx=Load()),
                                    attr='_compute_website_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create_and_redirect_configurator',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_force',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='configurator_action_todo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.website_configurator_todo', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='configurator_action_todo', ctx=Load()),
                                    attr='action_launch',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_website_api_rpc',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='route', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='params', ctx=Load()),
                                    slice=Constant(value='version', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='release', ctx=Load()),
                                attr='version',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrConfigParameter', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website_api_endpoint', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrConfigParameter', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website.website_api_endpoint', kind=None),
                                    Name(id='DEFAULT_ENDPOINT', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='endpoint', ctx=Store())],
                            value=BinOp(
                                left=Name(id='website_api_endpoint', ctx=Load()),
                                op=Add(),
                                right=Name(id='route', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='iap_tools', ctx=Load()),
                                    attr='iap_jsonrpc',
                                    ctx=Load(),
                                ),
                                args=[Name(id='endpoint', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Name(id='params', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_cta_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website_purpose', annotation=None, type_comment=None),
                            arg(arg='website_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='cta_btn_text', kind=None),
                                    Constant(value='cta_btn_href', kind=None),
                                ],
                                values=[
                                    Constant(value=False, kind=None),
                                    Constant(value='/contactus', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_theme_snippet_lists',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='theme_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='default_snippet_lists', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='http', ctx=Load()),
                                            attr='addons_manifest',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='theme_default', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='snippet_lists', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='theme_snippet_lists', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='http', ctx=Load()),
                                            attr='addons_manifest',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='theme_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='snippet_lists', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='snippet_lists', ctx=Store())],
                            value=Dict(
                                keys=[
                                    None,
                                    None,
                                ],
                                values=[
                                    Name(id='default_snippet_lists', ctx=Load()),
                                    Name(id='theme_snippet_lists', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='snippet_lists', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='configurator_set_menu_links',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='menu_company', annotation=None, type_comment=None),
                            arg(arg='module_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='menus', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.menu', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='module_data', ctx=Load()),
                                                                    attr='keys',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='m', ctx=Store()),
                            iter=Name(id='menus', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='m', ctx=Load()),
                                            attr='sequence',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='module_data', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='m', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sequence', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='configurator_get_footer_links',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='text', kind=None),
                                            Constant(value='href', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Privacy Policy', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='/privacy', kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='configurator_init',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='get_current_website',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='configurator_features', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.configurator.feature', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='r', ctx=Load()),
                                    slice=Constant(value='features', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='id', kind=None),
                                        Constant(value='name', kind=None),
                                        Constant(value='description', kind=None),
                                        Constant(value='type', kind=None),
                                        Constant(value='icon', kind=None),
                                        Constant(value='website_config_preselection', kind=None),
                                        Constant(value='module_state', kind=None),
                                    ],
                                    values=[
                                        Attribute(
                                            value=Name(id='feature', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='feature', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='feature', ctx=Load()),
                                            attr='description',
                                            ctx=Load(),
                                        ),
                                        IfExp(
                                            test=Attribute(
                                                value=Name(id='feature', ctx=Load()),
                                                attr='page_view_id',
                                                ctx=Load(),
                                            ),
                                            body=Constant(value='page', kind=None),
                                            orelse=Constant(value='app', kind=None),
                                        ),
                                        Attribute(
                                            value=Name(id='feature', ctx=Load()),
                                            attr='icon',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='feature', ctx=Load()),
                                            attr='website_config_preselection',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='feature', ctx=Load()),
                                                attr='module_id',
                                                ctx=Load(),
                                            ),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='feature', ctx=Store()),
                                        iter=Name(id='configurator_features', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='r', ctx=Load()),
                                    slice=Constant(value='logo', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='logo',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='logo',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='_get_logo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='r', ctx=Load()),
                                            slice=Constant(value='logo', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='logo',
                                                ctx=Load(),
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_website_api_rpc',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/api/website/1/configurator/industries', kind=None),
                                            Dict(
                                                keys=[Constant(value='lang', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='lang',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='r', ctx=Load()),
                                            slice=Constant(value='industries', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='industries', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AccessError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='r', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='configurator_recommended_themes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='industry_id', annotation=None, type_comment=None),
                            arg(arg='palette', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='=like', kind=None),
                                            Constant(value='theme%', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='not in', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='theme_default', kind=None),
                                                    Constant(value='theme_common', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='client_themes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.module.module', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='name', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='client_themes_img', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='t', ctx=Load()),
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='http', ctx=Load()),
                                                                attr='addons_manifest',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='t', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='images_preview_theme', kind=None),
                                                        Dict(keys=[], values=[]),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='t', ctx=Store()),
                                                iter=Name(id='client_themes', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='themes_suggested', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_website_api_rpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/api/website/2/configurator/recommended_themes/%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='industry_id', ctx=Load()),
                                    ),
                                    Dict(
                                        keys=[Constant(value='client_themes', kind=None)],
                                        values=[Name(id='client_themes_img', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='process_svg', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='website.configurator.feature', kind=None),
                                    ctx=Load(),
                                ),
                                attr='_process_svg',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='theme', ctx=Store()),
                            iter=Name(id='themes_suggested', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='theme', ctx=Load()),
                                            slice=Constant(value='svg', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='process_svg', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='theme', ctx=Load()),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='palette', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='theme', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='image_urls', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='themes_suggested', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='configurator_skip',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_current_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='configurator_done',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='configurator_apply',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='set_colors',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='selected_palette', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=Constant(value='/website/static/src/scss/options/user_values.scss', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='selected_palette_name', ctx=Store())],
                                    value=IfExp(
                                        test=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='selected_palette', ctx=Load()),
                                                Name(id='str', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        body=Name(id='selected_palette', ctx=Load()),
                                        orelse=Constant(value='base-1', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='color-palettes-name', kind=None)],
                                        values=[
                                            BinOp(
                                                left=Constant(value="'%s'", kind=None),
                                                op=Mod(),
                                                right=Name(id='selected_palette_name', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='web_editor.assets', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='make_scss_customization',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='url', ctx=Load()),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='selected_palette', ctx=Load()),
                                            Name(id='list', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='url', ctx=Store())],
                                            value=Constant(value='/website/static/src/scss/options/colors/user_color_palette.scss', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=DictComp(
                                                key=JoinedStr(
                                                    values=[
                                                        Constant(value='o-color-', kind=None),
                                                        FormattedValue(
                                                            value=Name(id='i', ctx=Load()),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                    ],
                                                ),
                                                value=Name(id='color', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='i', ctx=Store()),
                                                                Name(id='color', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Name(id='enumerate', ctx=Load()),
                                                            args=[
                                                                Name(id='selected_palette', ctx=Load()),
                                                                Constant(value=1, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='web_editor.assets', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='make_scss_customization',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='url', ctx=Load()),
                                                    Name(id='values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='set_features',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='selected_features', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='features', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.configurator.feature', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='selected_features', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='menu_company', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.menu', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='features', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='menu_sequence', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=5, kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='features', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='menu_company', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='menu_company', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website.menu', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='parent_id', kind=None),
                                                            Constant(value='website_id', kind=None),
                                                            Constant(value='sequence', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Company', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='website', ctx=Load()),
                                                                    attr='menu_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='website', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=40, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='pages_views', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='modules', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.module.module', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='module_data', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='feature', ctx=Store()),
                                    iter=Name(id='features', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='add_menu', ctx=Store())],
                                            value=Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='feature', ctx=Load()),
                                                        attr='menu_sequence',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='feature', ctx=Load()),
                                                attr='module_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='feature', ctx=Load()),
                                                                attr='module_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='installed', kind=None)],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='modules', ctx=Store()),
                                                            op=Add(),
                                                            value=Attribute(
                                                                value=Name(id='feature', ctx=Load()),
                                                                attr='module_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Name(id='add_menu', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='feature', ctx=Load()),
                                                                        attr='module_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='website_blog', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='module_data', ctx=Load()),
                                                                            slice=Attribute(
                                                                                value=Name(id='feature', ctx=Load()),
                                                                                attr='feature_url',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Dict(
                                                                        keys=[Constant(value='sequence', kind=None)],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='feature', ctx=Load()),
                                                                                attr='menu_sequence',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='blogs', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='module_data', ctx=Load()),
                                                                            attr='setdefault',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='#blog', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='blogs', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='name', kind=None),
                                                                                    Constant(value='sequence', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Name(id='feature', ctx=Load()),
                                                                                        attr='name',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='feature', ctx=Load()),
                                                                                        attr='menu_sequence',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='feature', ctx=Load()),
                                                        attr='page_view_id',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='result', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='website', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='new_page',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='name',
                                                                        value=Attribute(
                                                                            value=Name(id='feature', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='add_menu',
                                                                        value=Name(id='add_menu', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='page_values',
                                                                        value=Call(
                                                                            func=Name(id='dict', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='url',
                                                                                    value=Attribute(
                                                                                        value=Name(id='feature', ctx=Load()),
                                                                                        attr='feature_url',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                                keyword(
                                                                                    arg='is_published',
                                                                                    value=Constant(value=True, kind=None),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='menu_values',
                                                                        value=BoolOp(
                                                                            op=And(),
                                                                            values=[
                                                                                Name(id='add_menu', ctx=Load()),
                                                                                Dict(
                                                                                    keys=[
                                                                                        Constant(value='url', kind=None),
                                                                                        Constant(value='sequence', kind=None),
                                                                                        Constant(value='parent_id', kind=None),
                                                                                    ],
                                                                                    values=[
                                                                                        Attribute(
                                                                                            value=Name(id='feature', ctx=Load()),
                                                                                            attr='feature_url',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        Attribute(
                                                                                            value=Name(id='feature', ctx=Load()),
                                                                                            attr='menu_sequence',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        BoolOp(
                                                                                            op=Or(),
                                                                                            values=[
                                                                                                BoolOp(
                                                                                                    op=And(),
                                                                                                    values=[
                                                                                                        Attribute(
                                                                                                            value=Name(id='feature', ctx=Load()),
                                                                                                            attr='menu_company',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        Attribute(
                                                                                                            value=Name(id='menu_company', ctx=Load()),
                                                                                                            attr='id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ],
                                                                                                ),
                                                                                                Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='website', ctx=Load()),
                                                                                                        attr='menu_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='template',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='feature', ctx=Load()),
                                                                                attr='page_view_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='key',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='pages_views', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='feature', ctx=Load()),
                                                                        attr='iap_page_code',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='result', ctx=Load()),
                                                                slice=Constant(value='view_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='modules', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='modules', ctx=Load()),
                                                    attr='button_immediate_install',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assert(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='registry',
                                                    ctx=Load(),
                                                ),
                                                ops=[Is()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='registry', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            msg=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='website', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='configurator_set_menu_links',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='menu_company', ctx=Load()),
                                            Name(id='module_data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='pages_views', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='configure_page',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='page_code', annotation=None, type_comment=None),
                                    arg(arg='snippet_list', annotation=None, type_comment=None),
                                    arg(arg='pages_views', annotation=None, type_comment=None),
                                    arg(arg='cta_data', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='page_code', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='homepage', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='page_view_id', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='homepage_id',
                                                    ctx=Load(),
                                                ),
                                                attr='view_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='page_view_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.ui.view', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='pages_views', ctx=Load()),
                                                        slice=Name(id='page_code', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='rendered_snippets', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='nb_snippets', ctx=Store())],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='snippet_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='i', ctx=Store()),
                                            Name(id='snippet', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='snippet_list', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='start',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='view_id', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='website', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='website_id',
                                                                        value=Attribute(
                                                                            value=Name(id='website', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='viewref',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='website.', kind=None),
                                                                op=Add(),
                                                                right=Name(id='snippet', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='view_id', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='el', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='html', ctx=Load()),
                                                                    attr='fromstring',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='view_id', ctx=Load()),
                                                                            attr='_render',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='values',
                                                                                value=Name(id='cta_data', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='el', ctx=Load()),
                                                                        attr='attrib',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='data-snippet', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='snippet', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='i', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='shape_el', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='el', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value="//*[hasclass('o_we_shape')]", kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='shape_el', ctx=Load()),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Subscript(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='shape_el', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='attrib',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='class', kind=None),
                                                                                ctx=Store(),
                                                                            ),
                                                                            op=Add(),
                                                                            value=Constant(value=' o_header_extra_shape_mapping', kind=None),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='i', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='nb_snippets', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='shape_el', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='el', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value="//*[hasclass('o_we_shape')]", kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='shape_el', ctx=Load()),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Subscript(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='shape_el', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='attrib',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='class', kind=None),
                                                                                ctx=Store(),
                                                                            ),
                                                                            op=Add(),
                                                                            value=Constant(value=' o_footer_extra_shape_mapping', kind=None),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='rendered_snippet', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='pycompat', ctx=Load()),
                                                                    attr='to_text',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='etree', ctx=Load()),
                                                                            attr='tostring',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='el', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='rendered_snippets', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='rendered_snippet', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='ValueError', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='logger', ctx=Load()),
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='e', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='page_view_id', ctx=Load()),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='value',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Constant(value='', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='rendered_snippets', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='xpath',
                                                value=Constant(value="(//div[hasclass('oe_structure')])[last()]", kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='set_images',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='images', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='name', ctx=Store()),
                                            Name(id='url', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='images', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='response', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='requests', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='url', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='timeout',
                                                                value=Constant(value=3, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='response', ctx=Load()),
                                                            attr='raise_for_status',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='logger', ctx=Load()),
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Failed to download image: %s.\n%s', kind=None),
                                                                    Name(id='url', ctx=Load()),
                                                                    Name(id='e', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='attachment', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.attachment', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='website_id', kind=None),
                                                                    Constant(value='key', kind=None),
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='raw', kind=None),
                                                                    Constant(value='public', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='name', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='website', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='name', ctx=Load()),
                                                                    Constant(value='binary', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='response', ctx=Load()),
                                                                        attr='content',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.model.data', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='module', kind=None),
                                                                    Constant(value='model', kind=None),
                                                                    Constant(value='res_id', kind=None),
                                                                    Constant(value='noupdate', kind=None),
                                                                ],
                                                                values=[
                                                                    BinOp(
                                                                        left=Constant(value='configurator_%s_%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Attribute(
                                                                                    value=Name(id='website', ctx=Load()),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Subscript(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='name', ctx=Load()),
                                                                                            attr='split',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='.', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    slice=Constant(value=1, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Constant(value='website', kind=None),
                                                                    Constant(value='ir.attachment', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='attachment', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_current_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='theme_name', ctx=Store())],
                            value=Subscript(
                                value=Name(id='kwargs', ctx=Load()),
                                slice=Constant(value='theme_name', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='theme', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.module.module', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='theme_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='theme', ctx=Load()),
                                    attr='button_choose_theme',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[
                                    Call(
                                        func=Name(id='registry', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='configurator_done',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tour_asset_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.configurator_tour', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tour_asset_id', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='key', kind=None),
                                            Constant(value='website_id', kind=None),
                                            Constant(value='active', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='tour_asset_id', ctx=Load()),
                                                attr='key',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='website', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='logo_attachment_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='logo_attachment_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Attribute(
                                value=Name(id='website', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='logo_attachment_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.attachment', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='logo_attachment_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='res_field', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='website', kind=None),
                                                    Constant(value='logo', kind=None),
                                                    Attribute(
                                                        value=Name(id='website', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='logo_attachment_id', ctx=Load()),
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='logo',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='logo',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='company', ctx=Load()),
                                                            attr='_get_logo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='logo',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='logo',
                                                        ctx=Load(),
                                                    ),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='palette', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='selected_palette', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='palette', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='set_colors', ctx=Load()),
                                        args=[Name(id='palette', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='cta_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='get_cta_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website_purpose', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website_type', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='cta_data', ctx=Load()),
                                slice=Constant(value='cta_btn_text', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='xpath_view', ctx=Store())],
                                    value=Constant(value='website.snippets', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='parent_view', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='website_id',
                                                        value=Attribute(
                                                            value=Name(id='website', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='viewref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='xpath_view', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='key', kind=None),
                                                    Constant(value='inherit_id', kind=None),
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='priority', kind=None),
                                                    Constant(value='arch_db', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='parent_view', ctx=Load()),
                                                            attr='key',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value=' CTA', kind=None),
                                                    ),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='parent_view', ctx=Load()),
                                                            attr='key',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='_cta', kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='parent_view', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='website', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='qweb', kind=None),
                                                    Constant(value=32, kind=None),
                                                    BinOp(
                                                        left=Constant(value='\n                    <data>\n                        <xpath expr="//t[@t-set=\'cta_btn_href\']" position="replace">\n                            <t t-set="cta_btn_href">%s</t>\n                        </xpath>\n                        <xpath expr="//t[@t-set=\'cta_btn_text\']" position="replace">\n                            <t t-set="cta_btn_text">%s</t>\n                        </xpath>\n                    </data>\n                ', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Subscript(
                                                                    value=Name(id='cta_data', ctx=Load()),
                                                                    slice=Constant(value='cta_btn_href', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='cta_data', ctx=Load()),
                                                                    slice=Constant(value='cta_btn_text', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='view_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='viewref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='website.header_call_to_action', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='view_id', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='el', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='etree', ctx=Load()),
                                                            attr='fromstring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='view_id', ctx=Load()),
                                                                attr='arch_db',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='btn_cta_el', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value="//a[hasclass('btn_cta')]", kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='btn_cta_el', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='btn_cta_el', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='attrib',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='href', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='cta_data', ctx=Load()),
                                                                slice=Constant(value='cta_btn_href', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='btn_cta_el', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='text',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='cta_data', ctx=Load()),
                                                                slice=Constant(value='cta_btn_text', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='view_id', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='website_id',
                                                                        value=Attribute(
                                                                            value=Name(id='website', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='arch_db', kind=None)],
                                                                values=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='etree', ctx=Load()),
                                                                            attr='tostring',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='el', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='pages_views', ctx=Store())],
                            value=Call(
                                func=Name(id='set_features', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='selected_features', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='footer_links', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='configurator_get_footer_links',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='footer_ids', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='website.template_footer_contact', kind=None),
                                    Constant(value='website.template_footer_headline', kind=None),
                                    Constant(value='website.footer_custom', kind=None),
                                    Constant(value='website.template_footer_links', kind=None),
                                    Constant(value='website.template_footer_minimalist', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='footer_id', ctx=Store()),
                            iter=Name(id='footer_ids', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='view_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='viewref',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='footer_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='view_id', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='arch_string', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='etree', ctx=Load()),
                                                            attr='fromstring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='view_id', ctx=Load()),
                                                                attr='arch_db',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='el', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='arch_string', ctx=Load()),
                                                                attr='xpath',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value="//t[@t-set='configurator_footer_links']", kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='el', ctx=Load()),
                                                                attr='attrib',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='t-value', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='json', ctx=Load()),
                                                            attr='dumps',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='footer_links', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='view_id', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='website_id',
                                                                        value=Attribute(
                                                                            value=Name(id='website', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='arch_db', kind=None)],
                                                                values=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='etree', ctx=Load()),
                                                                            attr='tostring',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='arch_string', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='custom_resources', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_website_api_rpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/api/website/2/configurator/custom_resources/%s', kind=None),
                                        op=Mod(),
                                        right=Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='industry_id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Dict(
                                        keys=[Constant(value='theme', kind=None)],
                                        values=[Name(id='theme_name', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='requested_pages', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='pages_views', ctx=Load()),
                                                attr='keys',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[Constant(value='homepage', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='snippet_lists', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='get_theme_snippet_lists',
                                    ctx=Load(),
                                ),
                                args=[Name(id='theme_name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='page_code', ctx=Store()),
                            iter=Name(id='requested_pages', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='configure_page', ctx=Load()),
                                        args=[
                                            Name(id='page_code', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='snippet_lists', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='page_code', ctx=Load()),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='pages_views', ctx=Load()),
                                            Name(id='cta_data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='images', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='custom_resources', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='images', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='set_images', ctx=Load()),
                                args=[Name(id='images', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='url', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_bootstrap_homepage',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Page', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='website.page', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='standard_homepage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.homepage', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='standard_homepage', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='new_homepage_view', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='<t name="Homepage" t-name="website.homepage%s">\n    <t t-call="website.layout">\n        <t t-set="pageName" t-value="\'homepage\'"/>\n        <div id="wrap" class="oe_structure oe_empty"/>\n    </t>\n</t>', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='standard_homepage', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='website_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='arch_db',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='new_homepage_view', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='homepage_page', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Page', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='key', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='standard_homepage', ctx=Load()),
                                                        attr='key',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='homepage_page', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='homepage_page', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Page', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='website_published', kind=None),
                                                    Constant(value='url', kind=None),
                                                    Constant(value='view_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Constant(value='/', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='with_context',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='website_id',
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                attr='viewref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='website.homepage', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='homepage_page', ctx=Load()),
                                    attr='url',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='/', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='homepage_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='homepage_page', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default_menu', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.main_menu', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='copy_menu_hierarchy',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default_menu', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='home_menu', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.menu', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='/', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='home_menu', ctx=Load()),
                                    attr='page_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='homepage_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='copy_menu_hierarchy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='top_menu', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='copy_menu',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='menu', annotation=None, type_comment=None),
                                    arg(arg='t_menu', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_menu', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='menu', ctx=Load()),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='parent_id', kind=None),
                                                    Constant(value='website_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='t_menu', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='submenu', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='menu', ctx=Load()),
                                        attr='child_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='copy_menu', ctx=Load()),
                                                args=[
                                                    Name(id='submenu', ctx=Load()),
                                                    Name(id='new_menu', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='website', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='new_top_menu', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='top_menu', ctx=Load()),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='website_id', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Top Menu for Website %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='website', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='website', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='submenu', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='top_menu', ctx=Load()),
                                        attr='child_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='copy_menu', ctx=Load()),
                                                args=[
                                                    Name(id='submenu', ctx=Load()),
                                                    Name(id='new_top_menu', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='new_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='add_menu', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='ispage', annotation=None, type_comment=None),
                            arg(arg='namespace', annotation=None, type_comment=None),
                            arg(arg='page_values', annotation=None, type_comment=None),
                            arg(arg='menu_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value='website.default_page', kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create a new website page, and assign it a xmlid based on the given one\n            :param name : the name of the page\n            :param add_menu : if True, add a menu for that page\n            :param template : potential xml_id of the page to create\n            :param namespace : module part of the xml_id if none, the template module name is used\n            :param page_values : default values for the page to be created\n            :param menu_values : default values for the menu to be created\n        ', kind=None),
                        ),
                        If(
                            test=Name(id='namespace', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='template_module', ctx=Store())],
                                    value=Name(id='namespace', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='template_module', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='template', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='page_url', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='/', kind=None),
                                op=Add(),
                                right=Call(
                                    func=Name(id='slugify', ctx=Load()),
                                    args=[Name(id='name', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='max_length',
                                            value=Constant(value=1024, kind=None),
                                        ),
                                        keyword(
                                            arg='path',
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_unique_path',
                                    ctx=Load(),
                                ),
                                args=[Name(id='page_url', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page_key', ctx=Store())],
                            value=Call(
                                func=Name(id='slugify', ctx=Load()),
                                args=[Name(id='name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='url', kind=None)],
                                values=[Name(id='page_url', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='name', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Constant(value='Home', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page_key', ctx=Store())],
                                    value=Constant(value='home', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='template_record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Name(id='template', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_unique_key',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='page_key', ctx=Load()),
                                    Name(id='template_module', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='template_record', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='website_id', kind=None),
                                            Constant(value='key', kind=None),
                                        ],
                                        values=[
                                            Name(id='website_id', ctx=Load()),
                                            Name(id='key', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='arch', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='template_record', ctx=Load()),
                                                        attr='arch',
                                                        ctx=Load(),
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='template', ctx=Load()),
                                                    Name(id='key', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='name', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='view_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='view', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='view', ctx=Load()),
                                attr='arch_fs',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='view', ctx=Load()),
                                            attr='arch_fs',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_current_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='ispage', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='default_page_values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='url', kind=None),
                                            Constant(value='website_id', kind=None),
                                            Constant(value='view_id', kind=None),
                                            Constant(value='track', kind=None),
                                        ],
                                        values=[
                                            Name(id='page_url', ctx=Load()),
                                            Attribute(
                                                value=Name(id='website', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='page_values', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='default_page_values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='page_values', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='page', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.page', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='default_page_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='page_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='page', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='add_menu', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='default_menu_values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='url', kind=None),
                                            Constant(value='parent_id', kind=None),
                                            Constant(value='page_id', kind=None),
                                            Constant(value='website_id', kind=None),
                                        ],
                                        values=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='page_url', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='menu_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='page', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='website', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='menu_values', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='default_menu_values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='menu_values', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='menu', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.menu', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='default_menu_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='menu_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='menu', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='guess_mimetype',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='_guess_mimetype', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_unique_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page_url', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Given an url, return that url suffixed by counter if it already exists\n            :param page_url : the url to be checked for uniqueness\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='inc', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain_static', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='website_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='get_current_website',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page_temp', ctx=Store())],
                            value=Name(id='page_url', ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website.page', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='url', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='page_temp', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Name(id='domain_static', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='inc', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='page_temp', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='page_url', ctx=Load()),
                                        op=Add(),
                                        right=BoolOp(
                                            op=Or(),
                                            values=[
                                                BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='inc', ctx=Load()),
                                                        BinOp(
                                                            left=Constant(value='-%s', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='inc', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='page_temp', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_unique_key',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='string', annotation=None, type_comment=None),
                            arg(arg='template_module', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Given a string, return an unique key including module prefix.\n            It will be suffixed by a counter if it already exists to garantee uniqueness.\n            :param string : the key to be checked for uniqueness, you can pass it with 'website.' or not\n            :param template_module : the module to be prefixed on the key, if not set, we will use website\n        ", kind=None),
                        ),
                        If(
                            test=Name(id='template_module', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='string', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Name(id='template_module', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value='.', kind=None),
                                        ),
                                        op=Add(),
                                        right=Name(id='string', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='string', ctx=Load()),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='website.', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='string', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='website.', kind=None),
                                                op=Add(),
                                                right=Name(id='string', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='key_copy', ctx=Store())],
                            value=Name(id='string', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='inc', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain_static', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_current_website',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='website_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website.page', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='key', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='key_copy', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Name(id='domain_static', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='inc', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='key_copy', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='string', ctx=Load()),
                                        op=Add(),
                                        right=BoolOp(
                                            op=Or(),
                                            values=[
                                                BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='inc', ctx=Load()),
                                                        BinOp(
                                                            left=Constant(value='-%s', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='inc', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='key_copy', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='page_search_dependencies',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Search dependencies just for information. It will not catch 100%\n            of dependencies and False positive is more than possible\n            Each module could add dependences in this dict\n            :returns a dictionnary where key is the 'categorie' of object related to the given\n                view, and the value is the list of text and link to the resource using given page\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='dependencies', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='page_id', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='dependencies', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='page', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.page', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='page_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Attribute(
                                value=Name(id='page', ctx=Load()),
                                attr='url',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website_page_search_dom', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='view_id.arch_db', kind=None),
                                                Constant(value='ilike', kind=None),
                                                Name(id='url', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='website_domain',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pages', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.page', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='website_page_search_dom', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page_key', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Page', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='pages', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='page_key', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Pages', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='page_view_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='page', ctx=Store()),
                            iter=Name(id='pages', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dependencies', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_key', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='dependencies', ctx=Load()),
                                                slice=Name(id='page_key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='text', kind=None),
                                                    Constant(value='item', kind=None),
                                                    Constant(value='link', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Page <b>%s</b> contains a link to this page', kind=None),
                                                            Attribute(
                                                                value=Name(id='page', ctx=Load()),
                                                                attr='url',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='page', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='page', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='page_view_ids', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='view_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page_search_dom', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='arch_db', kind=None),
                                                Constant(value='ilike', kind=None),
                                                Name(id='url', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='id', kind=None),
                                                Constant(value='not in', kind=None),
                                                Name(id='page_view_ids', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='website_domain',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='views', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='page_search_dom', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view_key', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Template', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='views', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='view_key', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Templates', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='view', ctx=Store()),
                            iter=Name(id='views', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dependencies', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='view_key', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='dependencies', ctx=Load()),
                                                slice=Name(id='view_key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='text', kind=None),
                                                    Constant(value='link', kind=None),
                                                    Constant(value='item', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Template <b>%s (id:%s)</b> contains a link to this page', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='view', ctx=Load()),
                                                                            attr='key',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='view', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='view', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='/web#id=%s&view_type=form&model=ir.ui.view', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='view', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='%s (id:%s)', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='view', ctx=Load()),
                                                                            attr='key',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='view', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='view', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='menu_search_dom', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='url', kind=None),
                                                Constant(value='ilike', kind=None),
                                                BinOp(
                                                    left=Constant(value='%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='url', ctx=Load()),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='website_domain',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='menus', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.menu', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='menu_search_dom', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='menu_key', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Menu', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='menus', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='menu_key', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Menus', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='menu', ctx=Store()),
                            iter=Name(id='menus', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='dependencies', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='menu_key', ctx=Load()),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='text', kind=None),
                                                    Constant(value='link', kind=None),
                                                    Constant(value='item', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='This page is in the menu <b>%s</b>', kind=None),
                                                            Attribute(
                                                                value=Name(id='menu', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='/web#id=%s&view_type=form&model=website.menu', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='menu', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='menu', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='dependencies', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='page_search_key_dependencies',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Search dependencies just for information. It will not catch 100%\n            of dependencies and False positive is more than possible\n            Each module could add dependences in this dict\n            :returns a dictionnary where key is the 'categorie' of object related to the given\n                view, and the value is the list of text and link to the resource using given page\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='dependencies', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='page_id', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='dependencies', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='page', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.page', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='page_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=Attribute(
                                value=Name(id='page', ctx=Load()),
                                attr='key',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website_page_search_dom', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='view_id.arch_db', kind=None),
                                                Constant(value='ilike', kind=None),
                                                Name(id='key', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='id', kind=None),
                                                Constant(value='!=', kind=None),
                                                Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='website_domain',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pages', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.page', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='website_page_search_dom', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page_key', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Page', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='pages', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='page_key', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Pages', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='page_view_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='p', ctx=Store()),
                            iter=Name(id='pages', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dependencies', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_key', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='dependencies', ctx=Load()),
                                                slice=Name(id='page_key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='text', kind=None),
                                                    Constant(value='item', kind=None),
                                                    Constant(value='link', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Page <b>%s</b> is calling this file', kind=None),
                                                            Attribute(
                                                                value=Name(id='p', ctx=Load()),
                                                                attr='url',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='page_view_ids', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='view_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page_search_dom', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='arch_db', kind=None),
                                                Constant(value='ilike', kind=None),
                                                Name(id='key', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='id', kind=None),
                                                Constant(value='not in', kind=None),
                                                Name(id='page_view_ids', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='id', kind=None),
                                                Constant(value='!=', kind=None),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='page', ctx=Load()),
                                                        attr='view_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='website_domain',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='views', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='page_search_dom', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view_key', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Template', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='views', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='view_key', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Templates', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='view', ctx=Store()),
                            iter=Name(id='views', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dependencies', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='view_key', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='dependencies', ctx=Load()),
                                                slice=Name(id='view_key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='text', kind=None),
                                                    Constant(value='item', kind=None),
                                                    Constant(value='link', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Template <b>%s (id:%s)</b> is calling this file', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='view', ctx=Load()),
                                                                            attr='key',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='view', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='view', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='%s (id:%s)', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='view', ctx=Load()),
                                                                            attr='key',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='view', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='view', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='/web#id=%s&view_type=form&model=ir.ui.view', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='view', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='dependencies', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_alternate_languages',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='canonical_params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_is_canonical_url',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='canonical_params',
                                            value=Name(id='canonical_params', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='languages', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='language_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='languages', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[LtE()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='langs', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='shorts', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='lg', ctx=Store()),
                            iter=Name(id='languages', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='lg_codes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='lg', ctx=Load()),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='_', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='short', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='lg_codes', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='shorts', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='short', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='langs', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='hreflang', kind=None),
                                                    Constant(value='short', kind=None),
                                                    Constant(value='href', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Constant(value='-', kind=None),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='lg_codes', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='lower',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Name(id='short', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_canonical_url_localized',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='lang',
                                                                value=Name(id='lg', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='canonical_params',
                                                                value=Name(id='canonical_params', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='lang', ctx=Store()),
                            iter=Name(id='langs', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='shorts', ctx=Load()),
                                                attr='count',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='lang', ctx=Load()),
                                                    slice=Constant(value='short', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='lang', ctx=Load()),
                                                    slice=Constant(value='hreflang', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='lang', ctx=Load()),
                                                slice=Constant(value='short', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='langs', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='hreflang', kind=None),
                                            Constant(value='href', kind=None),
                                        ],
                                        values=[
                                            Constant(value='x-default', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_canonical_url_localized',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='lang',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='default_lang_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='canonical_params',
                                                        value=Name(id='canonical_params', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='langs', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_current_website',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fallback', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='request', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='force_website_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='website_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='session',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='force_website_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='website_id', ctx=Load()),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='force_website_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Name(id='website_id', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='website_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='website_id', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='website_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain_name', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='request', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='host',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country', ctx=Store())],
                            value=IfExp(
                                test=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id='request', ctx=Load()),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='geoip',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='geoip',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='country_code', kind=None)],
                                    keywords=[],
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country_id', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='country', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='country_id', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.country', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='code', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Name(id='country', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='limit',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='website_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_current_website_id',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain_name', ctx=Load()),
                                    Name(id='country_id', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='fallback',
                                        value=Name(id='fallback', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='website_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_current_website_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain_name', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                            arg(arg='fallback', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Get the current website id.\n\n        First find all the websites for which the configured `domain` (after\n        ignoring a potential scheme) is equal to the given\n        `domain_name`. If there is only one result, return it immediately.\n\n        If there are no website found for the given `domain_name`, either\n        fallback to the first found website (no matter its `domain`) or return\n        False depending on the `fallback` parameter.\n\n        If there are multiple websites for the same `domain_name`, we need to\n        filter them out by country. We return the first found website matching\n        the given `country_id`. If no found website matching `domain_name`\n        corresponds to the given `country_id`, the first found website for\n        `domain_name` will be returned (no matter its country).\n\n        :param domain_name: the domain for which we want the website.\n            In regard to the `url_parse` method, only the `netloc` part should\n            be given here, no `scheme`.\n        :type domain_name: string\n\n        :param country_id: id of the country for which we want the website\n        :type country_id: int\n\n        :param fallback: if True and no website is found for the specificed\n            `domain_name`, return the first website (without filtering them)\n        :type fallback: bool\n\n        :return: id of the found website, or False if no website is found and\n            `fallback` is False\n        :rtype: int or False\n\n        :raises: if `fallback` is True but no website at all is found\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='_remove_port',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='domain_name', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='domain_name', ctx=Load()),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=':', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_filter_domain',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='website', annotation=None, type_comment=None),
                                    arg(arg='domain_name', annotation=None, type_comment=None),
                                    arg(arg='ignore_port', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Constant(value=False, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value='Ignore `scheme` from the `domain`, just match the `netloc` which\n            is host:port in the version of `url_parse` we use.', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='website_domain', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='urls', ctx=Load()),
                                                attr='url_parse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='website', ctx=Load()),
                                                        attr='_get_http_domain',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='netloc',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='ignore_port', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='website_domain', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_remove_port', ctx=Load()),
                                                args=[Name(id='website_domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='domain_name', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_remove_port', ctx=Load()),
                                                args=[Name(id='domain_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='website_domain', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='domain_name', ctx=Load()),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='found_websites', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='domain', kind=None),
                                                            Constant(value='ilike', kind=None),
                                                            Call(
                                                                func=Name(id='_remove_port', ctx=Load()),
                                                                args=[Name(id='domain_name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='country_group_ids', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='websites', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='found_websites', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='w', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Name(id='_filter_domain', ctx=Load()),
                                            args=[
                                                Name(id='w', ctx=Load()),
                                                Name(id='domain_name', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='websites', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='websites', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='found_websites', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='w', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Call(
                                                    func=Name(id='_filter_domain', ctx=Load()),
                                                    args=[
                                                        Name(id='w', ctx=Load()),
                                                        Name(id='domain_name', ctx=Load()),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='ignore_port',
                                                            value=Constant(value=True, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='websites', ctx=Load()),
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='fallback', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[List(elts=[], ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='limit',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='websites', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Name(id='websites', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='country_specific_websites', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='websites', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='website', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Name(id='country_id', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='website', ctx=Load()),
                                                                                attr='country_group_ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='mapped',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='country_ids', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='ids',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=IfExp(
                                                test=Name(id='country_specific_websites', ctx=Load()),
                                                body=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='country_specific_websites', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                orelse=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='websites', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='cache',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='domain_name', kind=None),
                                Constant(value='country_id', kind=None),
                                Constant(value='fallback', kind=None),
                            ],
                            keywords=[],
                        ),
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_force',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_force_website',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_force_website',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Name(id='request', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='force_website_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='website_id', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='website_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='isdigit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='website_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_publisher',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.access', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='check',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.ui.view', kind=None),
                                    Constant(value='write', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.access', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='check',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.ui.menu', kind=None),
                                    Constant(value='read', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_public_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='website',
                                                ctx=Load(),
                                            ),
                                            attr='_get_cached',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='viewref',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='view_id', annotation=None, type_comment=None),
                            arg(arg='raise_if_not_found', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Given an xml_id or a view_id, return the corresponding view record.\n            In case of website context, return the most specific one.\n\n            If no website_id is in the context, it will return the generic view,\n            instead of a random one like `get_view_id`.\n\n            Look also for archived views, no matter the context.\n\n            :param view_id: either a string xml_id or an integer view_id\n            :param raise_if_not_found: should the method raise an error if no view found\n            :return: The view record or empty recordset\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='View', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=Name(id='View', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='view_id', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='website_id', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=BinOp(
                                                left=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='key', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Name(id='view_id', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='website', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='website_domain',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_context',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='website_id', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='order', ctx=Store())],
                                            value=Constant(value='website_id', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='key', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='view_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='order', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='View', ctx=Load()),
                                                attr='_order',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='views', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='View', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='order',
                                                value=Name(id='order', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='views', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='view', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='views', ctx=Load()),
                                                    attr='filter_duplicate',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='view', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='view_id', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='raise_if_not_found',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='view', ctx=Load()),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='view', ctx=Load()),
                                                            attr='_name',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='ir.ui.view', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='view', ctx=Store())],
                                                    value=Name(id='View', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='view_id', ctx=Load()),
                                            Name(id='int', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='view', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='View', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='view_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Expecting a string or an integer, not a %s.', kind=None),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Name(id='type', ctx=Load()),
                                                            args=[Name(id='view_id', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='view', ctx=Load()),
                                    ),
                                    Name(id='raise_if_not_found', ctx=Load()),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='No record found for unique ID %s. It may have been deleted.', kind=None),
                                                op=Mod(),
                                                right=Name(id='view_id', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='view', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_cache_customize_show_views',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='views', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.ui.view', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='customize_show', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='views', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='views', ctx=Load()),
                                    attr='filter_duplicate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='v', ctx=Load()),
                                    attr='key',
                                    ctx=Load(),
                                ),
                                value=Attribute(
                                    value=Name(id='v', ctx=Load()),
                                    attr='active',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='v', ctx=Store()),
                                        iter=Name(id='views', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache_context',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='keys',
                                    value=Tuple(
                                        elts=[Constant(value='website_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_view_active',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='raise_if_not_found', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n            Return True if active, False if not active, None if not found or not a customize_show view\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='views', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_cache_customize_show_views',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='key', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='views', ctx=Load())],
                                    ),
                                    Subscript(
                                        value=Name(id='views', ctx=Load()),
                                        slice=Name(id='key', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='view', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Name(id='raise_if_not_found', ctx=Load()),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='No view of type customize_show found for key %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='key', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='view', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache_context',
                                ctx=Load(),
                            ),
                            args=[Constant(value='key', kind=None)],
                            keywords=[
                                keyword(
                                    arg='keys',
                                    value=Tuple(
                                        elts=[Constant(value='website_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='View', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.ui.view', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='template', ctx=Load()),
                                    Name(id='int', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='view_id', ctx=Store())],
                                    value=Name(id='template', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Constant(value='.', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='template', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='template', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='website.%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='template', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='view_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='View', ctx=Load()),
                                            attr='get_view_id',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='view_id', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Name(id='NotFound', ctx=Load()),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='View', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='view_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='pager',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='total', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='step', annotation=None, type_comment=None),
                            arg(arg='scope', annotation=None, type_comment=None),
                            arg(arg='url_args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=1, kind=None),
                            Constant(value=30, kind=None),
                            Constant(value=5, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='pager', ctx=Load()),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Name(id='total', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='page',
                                        value=Name(id='page', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='step',
                                        value=Name(id='step', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='scope',
                                        value=Name(id='scope', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='url_args',
                                        value=Name(id='url_args', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='rule_is_enumerable',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Checks that it is possible to generate sensible GET queries for\n            a given rule (if the endpoint matches its own requirements)\n            :type rule: werkzeug.routing.Rule\n            :rtype: bool\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='endpoint', ctx=Store())],
                            value=Attribute(
                                value=Name(id='rule', ctx=Load()),
                                attr='endpoint',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='methods', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='endpoint', ctx=Load()),
                                                attr='routing',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='methods', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='converters', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='rule', ctx=Load()),
                                                attr='_converters',
                                                ctx=Load(),
                                            ),
                                            attr='values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Compare(
                                            left=Constant(value='GET', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='methods', ctx=Load())],
                                        ),
                                        Compare(
                                            left=Subscript(
                                                value=Attribute(
                                                    value=Name(id='endpoint', ctx=Load()),
                                                    attr='routing',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='type', kind=None),
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='http', kind=None)],
                                        ),
                                        Compare(
                                            left=Subscript(
                                                value=Attribute(
                                                    value=Name(id='endpoint', ctx=Load()),
                                                    attr='routing',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='auth', kind=None),
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='none', kind=None),
                                                        Constant(value='public', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='endpoint', ctx=Load()),
                                                    attr='routing',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='website', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Name(id='all', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Call(
                                                        func=Name(id='hasattr', ctx=Load()),
                                                        args=[
                                                            Name(id='converter', ctx=Load()),
                                                            Constant(value='generate', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='converter', ctx=Store()),
                                                            iter=Name(id='converters', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='sign', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='inspect', ctx=Load()),
                                    attr='signature',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='endpoint', ctx=Load()),
                                            attr='method',
                                            ctx=Load(),
                                        ),
                                        attr='original_func',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='sign', ctx=Load()),
                                                    attr='parameters',
                                                    ctx=Load(),
                                                ),
                                                attr='values',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='supported_kinds', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='inspect', ctx=Load()),
                                            attr='Parameter',
                                            ctx=Load(),
                                        ),
                                        attr='POSITIONAL_ONLY',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='inspect', ctx=Load()),
                                            attr='Parameter',
                                            ctx=Load(),
                                        ),
                                        attr='POSITIONAL_OR_KEYWORD',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='has_no_default', ctx=Store())],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='p', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=Compare(
                                    left=Attribute(
                                        value=Name(id='p', ctx=Load()),
                                        attr='default',
                                        ctx=Load(),
                                    ),
                                    ops=[Is()],
                                    comparators=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='inspect', ctx=Load()),
                                                attr='Parameter',
                                                ctx=Load(),
                                            ),
                                            attr='empty',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='all', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Attribute(
                                                value=Name(id='p', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='_converters',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='p', ctx=Store()),
                                                iter=Name(id='params', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='p', ctx=Load()),
                                                                    attr='kind',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='supported_kinds', ctx=Load())],
                                                            ),
                                                            Call(
                                                                func=Name(id='has_no_default', ctx=Load()),
                                                                args=[Name(id='p', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_enumerate_pages',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='query_string', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Available pages in the website/CMS. This is mostly used for links\n            generation and can be overridden by modules setting up new HTML\n            controllers for dynamic pages (e.g. blog).\n            By default, returns template views marked as pages.\n            :param str query_string: a (user-provided) string, fetches pages\n                                     matching the string\n            :returns: a list of mappings with two keys: ``name`` is the displayable\n                      name of the resource (page), ``url`` is the absolute URL\n                      of the same.\n            :rtype: list({name: str, url: str})\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='router', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='http', ctx=Load()),
                                        attr='root',
                                        ctx=Load(),
                                    ),
                                    attr='get_db_router',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url_set', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sitemap_endpoint_done', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rule', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='router', ctx=Load()),
                                    attr='iter_rules',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='sitemap', kind=None),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='endpoint',
                                                            ctx=Load(),
                                                        ),
                                                        attr='routing',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='endpoint',
                                                            ctx=Load(),
                                                        ),
                                                        attr='routing',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sitemap', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=True, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='endpoint',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='sitemap_endpoint_done', ctx=Load())],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sitemap_endpoint_done', ctx=Load()),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='rule', ctx=Load()),
                                                        attr='endpoint',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='func', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='rule', ctx=Load()),
                                                        attr='endpoint',
                                                        ctx=Load(),
                                                    ),
                                                    attr='routing',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='sitemap', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='func', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='loc', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='func', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='rule', ctx=Load()),
                                                    Name(id='query_string', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Yield(
                                                        value=Name(id='loc', ctx=Load()),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='rule_is_enumerable',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='rule', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='sitemap', kind=None),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='endpoint',
                                                    ctx=Load(),
                                                ),
                                                attr='routing',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='No Sitemap value provided for controller %s (%s)', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='rule', ctx=Load()),
                                                                        attr='endpoint',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='method',
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Constant(value=',', kind=None),
                                                                        attr='join',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='rule', ctx=Load()),
                                                                                    attr='endpoint',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='routing',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='routes', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='converters', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='rule', ctx=Load()),
                                                attr='_converters',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='query_string', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='converters', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Name(id='query_string', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='rule', ctx=Load()),
                                                                attr='build',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Dict(keys=[], values=[])],
                                                            keywords=[
                                                                keyword(
                                                                    arg='append_unknown',
                                                                    value=Constant(value=False, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=List(
                                        elts=[Dict(keys=[], values=[])],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='convitems', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='converters', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Tuple(
                                                        elts=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='hasattr', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='x', ctx=Load()),
                                                                                slice=Constant(value=1, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='domain', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='x', ctx=Load()),
                                                                                slice=Constant(value=1, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='domain',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[NotEq()],
                                                                        comparators=[Constant(value='[]', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='rule', ctx=Load()),
                                                                        attr='_trace',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='index',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=True, kind=None),
                                                                            Subscript(
                                                                                value=Name(id='x', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='i', ctx=Store()),
                                            Tuple(
                                                elts=[
                                                    Name(id='name', ctx=Store()),
                                                    Name(id='converter', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='convitems', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Constant(value='website_id', kind=None),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Attribute(
                                                                        value=Name(id='converter', ctx=Load()),
                                                                        attr='model',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_fields',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='converter', ctx=Load()),
                                                                    attr='domain',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='converter', ctx=Load()),
                                                                    attr='domain',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='[]', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='converter', ctx=Load()),
                                                            attr='domain',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value="[('website_id', 'in', (False, current_website_id))]", kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='newval', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='val', ctx=Store()),
                                            iter=Name(id='values', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='query', ctx=Store())],
                                                    value=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='i', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    BinOp(
                                                                        left=Call(
                                                                            func=Name(id='len', ctx=Load()),
                                                                            args=[Name(id='convitems', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Sub(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='query_string', ctx=Load()),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='query', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='r', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Constant(value='', kind=None),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    ListComp(
                                                                        elt=Subscript(
                                                                            value=Name(id='x', ctx=Load()),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='x', ctx=Store()),
                                                                                iter=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='rule', ctx=Load()),
                                                                                        attr='_trace',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Slice(
                                                                                        lower=Constant(value=1, kind=None),
                                                                                        upper=None,
                                                                                        step=None,
                                                                                    ),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ifs=[
                                                                                    UnaryOp(
                                                                                        op=Not(),
                                                                                        operand=Subscript(
                                                                                            value=Name(id='x', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='query', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='sitemap_qs2dom', ctx=Load()),
                                                                args=[
                                                                    Name(id='query', ctx=Load()),
                                                                    Name(id='r', ctx=Load()),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Attribute(
                                                                                value=Name(id='converter', ctx=Load()),
                                                                                attr='model',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='_rec_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='query', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='FALSE_DOMAIN', ctx=Load())],
                                                            ),
                                                            body=[Continue()],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                For(
                                                    target=Name(id='rec', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='converter', ctx=Load()),
                                                            attr='generate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='uid',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='uid',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='dom',
                                                                value=Name(id='query', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='args',
                                                                value=Name(id='val', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='newval', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='val', ctx=Load()),
                                                                            attr='copy',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='newval', ctx=Load()),
                                                                        slice=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Constant(value=1, kind=None),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[Name(id='name', ctx=Load())],
                                                                        values=[Name(id='rec', ctx=Load())],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Name(id='newval', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='value', ctx=Store()),
                                    iter=Name(id='values', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='domain_part', ctx=Store()),
                                                        Name(id='url', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='build',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='append_unknown',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='query_string', ctx=Load()),
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='query_string', ctx=Load()),
                                                                attr='lower',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='url', ctx=Load()),
                                                                    attr='lower',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='page', ctx=Store())],
                                                    value=Dict(
                                                        keys=[Constant(value='loc', kind=None)],
                                                        values=[Name(id='url', ctx=Load())],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='url', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='url_set', ctx=Load())],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='url_set', ctx=Load()),
                                                            attr='add',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='url', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Yield(
                                                        value=Name(id='page', ctx=Load()),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='url', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value='/', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='force', ctx=Load()),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_indexed', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='visibility', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_published', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='visibility', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_publish', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_publish', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='now',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='query_string', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Name(id='query_string', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='pages', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_website_pages',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='page', ctx=Store()),
                            iter=Name(id='pages', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='loc', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Subscript(
                                                value=Name(id='page', ctx=Load()),
                                                slice=Constant(value='url', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='page', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='page', ctx=Load()),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='page', ctx=Load()),
                                                attr='view_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='page', ctx=Load()),
                                                        attr='view_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='priority',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=16, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='record', ctx=Load()),
                                                    slice=Constant(value='priority', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='round', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='page', ctx=Load()),
                                                                        attr='view_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='priority',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Div(),
                                                                right=Constant(value=32.0, kind=None),
                                                            ),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='page', ctx=Load()),
                                        slice=Constant(value='write_date', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='record', ctx=Load()),
                                                    slice=Constant(value='lastmod', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='page', ctx=Load()),
                                                        slice=Constant(value='write_date', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='date',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Yield(
                                        value=Name(id='record', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_website_pages',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='name', kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='domain', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='domain', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_current_website',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='website_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='pages', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.page', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Name(id='order', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='pages', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='search_pages',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='needle', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Call(
                                func=Name(id='slugify', ctx=Load()),
                                args=[Name(id='needle', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='max_length',
                                        value=Constant(value=50, kind=None),
                                    ),
                                    keyword(
                                        arg='path',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='page', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_enumerate_pages',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='query_string',
                                        value=Name(id='name', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='force',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='page', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='res', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='limit', ctx=Load())],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_suggested_controllers',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n            Returns a tuple (name, url, icon).\n            Where icon can be a module name, or a path\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='suggested_controllers', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Homepage', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='url_for', ctx=Load()),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='website', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Contact Us', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='url_for', ctx=Load()),
                                                args=[Constant(value='/contactus', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='website_crm', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='suggested_controllers', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='image_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns a local url that points to the image field of a given browse record. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sudo_record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sha', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='hashlib', ctx=Load()),
                                                attr='sha512',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='getattr', ctx=Load()),
                                                                    args=[
                                                                        Name(id='sudo_record', ctx=Load()),
                                                                        Constant(value='__last_update', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='utf-8', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='hexdigest',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Slice(
                                    lower=None,
                                    upper=Constant(value=7, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='size', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='size', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Constant(value='', kind=None),
                                orelse=BinOp(
                                    left=Constant(value='/%s', kind=None),
                                    op=Mod(),
                                    right=Name(id='size', ctx=Load()),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='/web/image/%s/%s/%s%s?unique=%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Name(id='field', ctx=Load()),
                                        Name(id='size', ctx=Load()),
                                        Name(id='sha', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_cdn_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='uri', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='uri', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='cdn_url', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='cdn_url',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cdn_filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cdn_filters',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    attr='splitlines',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='flt', ctx=Store()),
                            iter=Name(id='cdn_filters', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='flt', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='match',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='flt', ctx=Load()),
                                                    Name(id='uri', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='urls', ctx=Load()),
                                                    attr='url_join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cdn_url', ctx=Load()),
                                                    Name(id='uri', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='uri', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_dashboard_redirect',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.group_system', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website.group_website_designer', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.actions.actions', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_for_xml_id',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website.backend_dashboard', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.action_website', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='button_go_website',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='mode_edit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='/', kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_force',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='mode_edit', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='path', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='?enable_editor=1', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='url', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_url', kind=None),
                                    Name(id='path', ctx=Load()),
                                    Constant(value='self', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_http_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Get the domain of the current website, prefixed by http if no\n        scheme is specified.\n\n        Empty string if no domain is specified on the website.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='domain',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urls', ctx=Load()),
                                    attr='url_parse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='domain',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Attribute(
                                        value=Name(id='res', ctx=Load()),
                                        attr='scheme',
                                        ctx=Load(),
                                    ),
                                ),
                                body=BinOp(
                                    left=Constant(value='http://', kind=None),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='domain',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='domain',
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_canonical_url_localized',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lang', annotation=None, type_comment=None),
                            arg(arg='canonical_params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns the canonical URL for the current request with translatable\n        elements appropriately translated in `lang`.\n\n        If `request.endpoint` is not true, returns the current `path` instead.\n\n        `url_quote_plus` is applied on the returned path.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='endpoint',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='router', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='http', ctx=Load()),
                                                        attr='root',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_db_router',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='db',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='bind',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='arguments', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='endpoint_arguments',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='key', ctx=Store()),
                                            Name(id='val', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='arguments', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='val', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='models', ctx=Load()),
                                                        attr='BaseModel',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='val', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='context',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='lang', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='lang', ctx=Load()),
                                                                attr='code',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='arguments', ctx=Load()),
                                                                    slice=Name(id='key', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='val', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='lang',
                                                                        value=Attribute(
                                                                            value=Name(id='lang', ctx=Load()),
                                                                            attr='code',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='router', ctx=Load()),
                                            attr='build',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='endpoint',
                                                ctx=Load(),
                                            ),
                                            Name(id='arguments', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='urls', ctx=Load()),
                                            attr='url_quote_plus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='safe',
                                                value=Constant(value='/', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='lang_path', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='lang', ctx=Load()),
                                    ops=[NotEq()],
                                    comparators=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='default_lang_id',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=BinOp(
                                    left=Constant(value='/', kind=None),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='lang', ctx=Load()),
                                        attr='url_code',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='canonical_query_string', ctx=Store())],
                            value=IfExp(
                                test=Name(id='canonical_params', ctx=Load()),
                                body=BinOp(
                                    left=Constant(value='?%s', kind=None),
                                    op=Mod(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='urls', ctx=Load()),
                                            attr='url_encode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='canonical_params', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='get_base_url',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Name(id='lang_path', ctx=Load()),
                                    ),
                                    op=Add(),
                                    right=Name(id='path', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='canonical_query_string', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_canonical_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='canonical_params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns the canonical URL for the current request.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_canonical_url_localized',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='lang',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='canonical_params',
                                        value=Name(id='canonical_params', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_canonical_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='canonical_params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns whether the current request URL is canonical.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='args',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='canonical_params', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='canonical_params', ctx=Load()),
                                    Call(
                                        func=Name(id='OrderedMultiDict', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='params', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Name(id='canonical_params', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='current_url', ctx=Store())],
                            value=BinOp(
                                left=Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='url_root',
                                        ctx=Load(),
                                    ),
                                    slice=Slice(
                                        lower=None,
                                        upper=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=BoolOp(
                                    op=Or(),
                                    values=[
                                        BoolOp(
                                            op=And(),
                                            values=[
                                                Call(
                                                    func=Name(id='hasattr', ctx=Load()),
                                                    args=[
                                                        Name(id='request', ctx=Load()),
                                                        Constant(value='rerouting', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='rerouting',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='canonical_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_canonical_url_localized',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='lang',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='canonical_params',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Compare(
                                left=Name(id='current_url', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='canonical_url', ctx=Load())],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_cached_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='user_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='default_lang_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='default_lang_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache',
                                ctx=Load(),
                            ),
                            args=[Constant(value='self.id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_cached',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_cached_values',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Name(id='field', ctx=Load()),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_html_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html_fields', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='ir_ui_view', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cr', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='cr',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="\n            SELECT f.model,\n                   f.name\n              FROM ir_model_fields f\n              JOIN ir_model m\n                ON m.id = f.model_id\n             WHERE f.ttype = 'html'\n               AND f.store = true\n               AND m.transient = false\n               AND f.model NOT LIKE 'ir.actions%'\n               AND f.model != 'mail.message'\n        ", kind=None)],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='model', ctx=Store()),
                                    Name(id='name', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='table', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='model', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        attr='_table',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='table_exists',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='table', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='column_exists',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='table', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='html_fields', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='table', ctx=Load()),
                                                            Name(id='name', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='html_fields', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_snippets_assets',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Returns every parent snippet asset from the database, filtering out\n        their potential overrides defined in other modules. As they share the same\n        snippet_id, asset_version and asset_type, it is possible to do that using\n        Postgres' DISTINCT ON and ordering by asset_id, as overriden assets will be\n        created later than their parents.\n        The assets are returned in the form of a list of tuples :\n        [(snippet_module, snippet_id, asset_version, asset_type, asset_id)]\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="\n            SELECT DISTINCT ON (snippet_id, asset_version, asset_type)\n                   regexp_matches[1] AS snippet_module,\n                   regexp_matches[2] AS snippet_id,\n                   regexp_matches[3] AS asset_version,\n                   CASE\n                       WHEN regexp_matches[4]='scss' THEN 'css'\n                       ELSE regexp_matches[4]\n                   END AS asset_type,\n                   id AS asset_id\n            FROM (\n                SELECT REGEXP_MATCHES(PATH, '(\\w*)\\/.*\\/snippets\\/(\\w*)\\/(\\d{3})\\.(js|scss)'),\n                       id\n                FROM ir_asset\n            ) AS regexp\n            ORDER BY snippet_id, asset_version, asset_type, asset_id;\n        ", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_snippet_used',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='snippet_module', annotation=None, type_comment=None),
                            arg(arg='snippet_id', annotation=None, type_comment=None),
                            arg(arg='asset_version', annotation=None, type_comment=None),
                            arg(arg='asset_type', annotation=None, type_comment=None),
                            arg(arg='html_fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='snippet_occurences', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='snippet_template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    JoinedStr(
                                        values=[
                                            FormattedValue(
                                                value=Name(id='snippet_module', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='.', kind=None),
                                            FormattedValue(
                                                value=Name(id='snippet_id', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='snippet_template', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='snippet_template_html', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='snippet_template', ctx=Load()),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='<([^>]*class="[^>]*)>', kind=None),
                                            Name(id='snippet_template_html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='snippet_occurences', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='match', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='snippet_regex', ctx=Store())],
                            value=JoinedStr(
                                values=[
                                    Constant(value='<([^>]*data-snippet="', kind=None),
                                    FormattedValue(
                                        value=Name(id='snippet_id', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value='"[^>]*)>', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='snippet_dropped', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='UNION ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=JoinedStr(
                                            values=[
                                                Constant(value='SELECT REGEXP_MATCHES(', kind=None),
                                                FormattedValue(
                                                    value=Name(id='column', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value=", '", kind=None),
                                                FormattedValue(
                                                    value=Name(id='snippet_regex', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value="') FROM ", kind=None),
                                                FormattedValue(
                                                    value=Name(id='table', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value=' ', kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='table', ctx=Store()),
                                                        Name(id='column', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Name(id='html_fields', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Name(id='snippet_dropped', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='r', ctx=Store()),
                            iter=Name(id='results', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='snippet_occurences', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='r', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='snippet', ctx=Store()),
                            iter=Name(id='snippet_occurences', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='asset_version', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='000', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=JoinedStr(
                                                    values=[
                                                        Constant(value='data-v', kind=None),
                                                        FormattedValue(
                                                            value=Name(id='asset_type', ctx=Load()),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                    ],
                                                ),
                                                ops=[NotIn()],
                                                comparators=[Name(id='snippet', ctx=Load())],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=JoinedStr(
                                                    values=[
                                                        Constant(value='data-v', kind=None),
                                                        FormattedValue(
                                                            value=Name(id='asset_type', ctx=Load()),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                        Constant(value='="', kind=None),
                                                        FormattedValue(
                                                            value=Name(id='asset_version', ctx=Load()),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                        Constant(value='"', kind=None),
                                                    ],
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='snippet', ctx=Load())],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_disable_unused_snippets_assets',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='snippets_assets', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_snippets_assets',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_html_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='snippet_module', ctx=Store()),
                                    Name(id='snippet_id', ctx=Store()),
                                    Name(id='asset_version', ctx=Store()),
                                    Name(id='asset_type', ctx=Store()),
                                    Name(id='_', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='snippets_assets', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='is_snippet_used', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_snippet_used',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='snippet_module', ctx=Load()),
                                            Name(id='snippet_id', ctx=Load()),
                                            Name(id='asset_version', ctx=Load()),
                                            Name(id='asset_type', ctx=Load()),
                                            Name(id='html_fields', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='filename_type', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='asset_type', ctx=Load()),
                                            ops=[Eq()],
                                            comparators=[Constant(value='css', kind=None)],
                                        ),
                                        body=Constant(value='scss', kind=None),
                                        orelse=Name(id='asset_type', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='assets_path', ctx=Store())],
                                    value=JoinedStr(
                                        values=[
                                            FormattedValue(
                                                value=Name(id='snippet_id', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='/', kind=None),
                                            FormattedValue(
                                                value=Name(id='asset_version', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='.', kind=None),
                                            FormattedValue(
                                                value=Name(id='filename_type', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\n                UPDATE ir_asset\n                SET active = %(active)s\n                WHERE path ~ %(assets_path)s\n            ', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='assets_path', kind=None),
                                                ],
                                                values=[
                                                    Name(id='is_snippet_used', ctx=Load()),
                                                    Name(id='assets_path', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='autovacuum',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_build_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Builds a search domain AND-combining a base domain with partial matches of each term in\n        the search expression in any of the fields.\n\n        :param domain: base domain combined in the search expression\n        :param search: search expression string\n        :param fields: list of field names to match the terms of the search expression with\n        :param extra: function that returns an additional subdomain for a search term\n\n        :return: domain limited to the matches of the search expression\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='domains', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='domain', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='search', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='search_term', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='search', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=' ', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='subdomains', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='field', ctx=Store()),
                                            iter=Name(id='fields', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subdomains', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='field', ctx=Load()),
                                                                            Constant(value='ilike', kind=None),
                                                                            Call(
                                                                                func=Name(id='escape_psql', ctx=Load()),
                                                                                args=[Name(id='search_term', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='extra', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subdomains', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='extra', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='search_term', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='domains', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='OR', ctx=Load()),
                                                        args=[Name(id='subdomains', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='AND', ctx=Load()),
                                args=[Name(id='domains', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_text_from_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='html_fragment', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Returns the plain non-tag text from an html\n\n        :param html_fragment: document from which text must be extracted\n\n        :return text extracted from the html\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tree', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='<p>%s</p>', kind=None),
                                        op=Mod(),
                                        right=Name(id='html_fragment', ctx=Load()),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='XMLParser',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='recover',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='itertext',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_get_details',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_type', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Returns indications on how to perform the searches\n\n        :param search_type: type of search\n        :param order: order in which the results are to be returned\n        :param options: search options\n\n        :return: list of search details obtained from the `website.searchable.mixin`'s `_search_get_detail()`\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='search_type', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='pages', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website.page', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_search_get_detail',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='order', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_with_fuzzy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_type', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Performs a search with a search text or with a resembling word\n\n        :param search_type: indicates what to search within, 'all' matches all available types\n        :param search: text against which to match results\n        :param limit: maximum number of results per model type involved in the result\n        :param order: order on which to sort results within a model type\n        :param options: search options from the submitted form containing:\n            - allowFuzzy: boolean indicating whether the fuzzy matching must be done\n            - other options used by `_search_get_details()`\n\n        :return: tuple containing:\n            - count: total number of results across all involved models\n            - results: list of results per model (see _search_exact)\n            - fuzzy_term: similar word against which results were obtained, indicates there were\n                no results for the initially requested search\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='fuzzy_term', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='search_details', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_search_get_details',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='search_type', ctx=Load()),
                                    Name(id='order', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='search', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='allowFuzzy', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fuzzy_term', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_find_fuzzy_term',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='search_details', ctx=Load()),
                                            Name(id='search', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='fuzzy_term', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='count', ctx=Store()),
                                                        Name(id='results', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_search_exact',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='search_details', ctx=Load()),
                                                    Name(id='fuzzy_term', ctx=Load()),
                                                    Name(id='limit', ctx=Load()),
                                                    Name(id='order', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='fuzzy_term', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Name(id='search', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='fuzzy_term', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='count', ctx=Store()),
                                                        Name(id='results', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_search_exact',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='search_details', ctx=Load()),
                                                    Name(id='search', ctx=Load()),
                                                    Name(id='limit', ctx=Load()),
                                                    Name(id='order', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='count', ctx=Store()),
                                                Name(id='results', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_exact',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='search_details', ctx=Load()),
                                            Name(id='search', ctx=Load()),
                                            Name(id='limit', ctx=Load()),
                                            Name(id='order', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='count', ctx=Load()),
                                    Name(id='results', ctx=Load()),
                                    Name(id='fuzzy_term', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_exact',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_details', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Performs a search with a search text\n\n        :param search_details: see :meth:`_search_get_details`\n        :param search: text against which to match results\n        :param limit: maximum number of results per model type involved in the result\n        :param order: order on which to sort results within a model type\n\n        :return: tuple containing:\n            - total number of results across all involved models\n            - list of results per model made of:\n                - initial search_detail for the model\n                - count: number of results for the model\n                - results: model list equivalent to a `model.search()`\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='all_results', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total_count', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='search_detail', ctx=Store()),
                            iter=Name(id='search_details', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Subscript(
                                            value=Name(id='search_detail', ctx=Load()),
                                            slice=Constant(value='model', kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='results', ctx=Store()),
                                                Name(id='count', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='_search_fetch',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='search_detail', ctx=Load()),
                                            Name(id='search', ctx=Load()),
                                            Name(id='limit', ctx=Load()),
                                            Name(id='order', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='search_detail', ctx=Load()),
                                            slice=Constant(value='results', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='results', ctx=Load()),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='total_count', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='count', ctx=Load()),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='search_detail', ctx=Load()),
                                            slice=Constant(value='count', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='count', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='all_results', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='search_detail', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='total_count', ctx=Load()),
                                    Name(id='all_results', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_render_results',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_details', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Prepares data for the autocomplete and hybrid list rendering\n\n        :param search_details: obtained from `_search_exact()`\n        :param limit: maximum number or rows to render\n\n        :return: the updated `search_details` containing an additional `results_data` field equivalent\n            to the result of a `model.read()`\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='search_detail', ctx=Store()),
                            iter=Name(id='search_details', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='search_detail', ctx=Load()),
                                        slice=Constant(value='fetch_fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='results', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='search_detail', ctx=Load()),
                                        slice=Constant(value='results', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='icon', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='search_detail', ctx=Load()),
                                        slice=Constant(value='icon', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mapping', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='search_detail', ctx=Load()),
                                        slice=Constant(value='mapping', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='results_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='results', ctx=Load()),
                                            attr='_search_render_results',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fields', ctx=Load()),
                                            Name(id='mapping', ctx=Load()),
                                            Name(id='icon', ctx=Load()),
                                            Name(id='limit', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='search_detail', ctx=Load()),
                                            slice=Constant(value='results_data', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='results_data', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='search_details', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_find_fuzzy_term',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_details', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='word_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=1000, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Returns the "closest" match of the search parameter within available words.\n\n        :param search_details: obtained from `_search_get_details()`\n        :param search: search term to which words must be matched against\n        :param limit: maximum number of records fetched per model to build the word list\n        :param word_list: if specified, this list of words is used as possible targets instead of\n            the words contained in the match fields of each involved model\n\n        :return: term on which a search can be performed instead of the initial search\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='search', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=4, kind=None)],
                                    ),
                                    Compare(
                                        left=Constant(value=' ', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='search', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='search', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='search', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='search', ctx=Load()),
                                    attr='lower',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='words', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='best_score', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='best_word', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='enumerate_words', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='has_trigram',
                                    ctx=Load(),
                                ),
                                body=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_trigram_enumerate_words',
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_basic_enumerate_words',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='word', ctx=Store()),
                            iter=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='word_list', ctx=Load()),
                                    Call(
                                        func=Name(id='enumerate_words', ctx=Load()),
                                        args=[
                                            Name(id='search_details', ctx=Load()),
                                            Name(id='search', ctx=Load()),
                                            Name(id='limit', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='search', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='word', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='search', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='word', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='search', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id='word', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='words', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='similarity', ctx=Store())],
                                            value=Call(
                                                func=Name(id='similarity_score', ctx=Load()),
                                                args=[
                                                    Name(id='search', ctx=Load()),
                                                    Name(id='word', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='similarity', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Name(id='best_score', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='best_score', ctx=Store())],
                                                    value=Name(id='similarity', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='best_word', ctx=Store())],
                                                    value=Name(id='word', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='words', ctx=Load()),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='word', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='best_word', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_trigram_enumerate_words',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_details', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Browses through all words that need to be compared to the search term.\n        It extracts all words of every field associated to models in the fields_per_model parameter.\n        The search is restricted to a records having the non-zero pg_trgm.word_similarity() score.\n\n        :param search_details: obtained from `_search_get_details()`\n        :param search: search term to which words must be matched against\n        :param limit: maximum number of records fetched per model to build the word list\n        :return: yields words\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='match_pattern', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='\\w{%s,}', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Name(id='min', ctx=Load()),
                                    args=[
                                        Constant(value=4, kind=None),
                                        BinOp(
                                            left=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='search', ctx=Load())],
                                                keywords=[],
                                            ),
                                            op=Sub(),
                                            right=Constant(value=3, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='similarity_threshold', ctx=Store())],
                            value=Constant(value=0.3, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='search_detail', ctx=Store()),
                            iter=Name(id='search_details', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='model_name', ctx=Store()),
                                                Name(id='fields', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Subscript(
                                                value=Name(id='search_detail', ctx=Load()),
                                                slice=Constant(value='model', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='search_detail', ctx=Load()),
                                                slice=Constant(value='search_fields', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='search_detail', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='requires_sudo', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='model', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='model', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='search_detail', ctx=Load()),
                                                slice=Constant(value='base_domain', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[Name(id='fields', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='intersection',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='unaccent', ctx=Store())],
                                    value=Call(
                                        func=Name(id='get_unaccent_sql_wrapper', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='similarities', ctx=Store())],
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='SQL',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='word_similarity({search}, {field})', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='format',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='search',
                                                    value=Call(
                                                        func=Name(id='unaccent', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='sql', ctx=Load()),
                                                                    attr='Placeholder',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='search', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='field',
                                                    value=Call(
                                                        func=Name(id='unaccent', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='sql', ctx=Load()),
                                                                            attr='SQL',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='{table}.{field}', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='format',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='table',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='sql', ctx=Load()),
                                                                                attr='Identifier',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=IfExp(
                                                                                        test=BoolOp(
                                                                                            op=Or(),
                                                                                            values=[
                                                                                                Compare(
                                                                                                    left=Name(id='field', ctx=Load()),
                                                                                                    ops=[Eq()],
                                                                                                    comparators=[Constant(value='arch_db', kind=None)],
                                                                                                ),
                                                                                                BoolOp(
                                                                                                    op=And(),
                                                                                                    values=[
                                                                                                        Compare(
                                                                                                            left=Name(id='field', ctx=Load()),
                                                                                                            ops=[Eq()],
                                                                                                            comparators=[Constant(value='name', kind=None)],
                                                                                                        ),
                                                                                                        Compare(
                                                                                                            left=Constant(value='arch_db', kind=None),
                                                                                                            ops=[In()],
                                                                                                            comparators=[Name(id='fields', ctx=Load())],
                                                                                                        ),
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                        body=Subscript(
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='env',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            slice=Constant(value='ir.ui.view', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        orelse=Name(id='model', ctx=Load()),
                                                                                    ),
                                                                                    attr='_table',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='field',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='sql', ctx=Load()),
                                                                                attr='Identifier',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='field', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field', ctx=Store()),
                                                iter=Name(id='fields', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='best_similarity', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='GREATEST({similarities})', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='similarities',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='sql', ctx=Load()),
                                                                attr='SQL',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=', ', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='similarities', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='from_clause', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='FROM {table}', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='table',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Identifier',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='model', ctx=Load()),
                                                            attr='_table',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='arch_db', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='from_clause', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='sql', ctx=Load()),
                                                            attr='SQL',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='\n                    {from_clause}\n                    LEFT JOIN {view_table} ON {table}.view_id = {view_table}.id\n                ', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='from_clause',
                                                        value=Name(id='from_clause', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='table',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='sql', ctx=Load()),
                                                                attr='Identifier',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='model', ctx=Load()),
                                                                    attr='_table',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='view_table',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='sql', ctx=Load()),
                                                                attr='Identifier',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='ir.ui.view', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_table',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='\n                SELECT {table}.id, {best_similarity} AS _best_similarity\n                {from_clause}\n                ORDER BY _best_similarity desc\n                LIMIT 1000\n            ', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='table',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Identifier',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='model', ctx=Load()),
                                                            attr='_table',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='best_similarity',
                                                value=Name(id='best_similarity', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='from_clause',
                                                value=Name(id='from_clause', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='query', ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='search', kind=None)],
                                                values=[Name(id='search', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='ids', ctx=Store())],
                                    value=SetComp(
                                        elt=Subscript(
                                            value=Name(id='row', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='row', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='cr',
                                                            ctx=Load(),
                                                        ),
                                                        attr='fetchall',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[GtE()],
                                                        comparators=[Name(id='similarity_threshold', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='lang',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='arch_db', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='fields', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='similarity', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='sql', ctx=Load()),
                                                                    attr='SQL',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='word_similarity({search}, {field})', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='search',
                                                                value=Call(
                                                                    func=Name(id='unaccent', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='sql', ctx=Load()),
                                                                                attr='Placeholder',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='search', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='field',
                                                                value=Call(
                                                                    func=Name(id='unaccent', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='sql', ctx=Load()),
                                                                                attr='SQL',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='t.value', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='names', ctx=Store())],
                                                    value=ListComp(
                                                        elt=BinOp(
                                                            left=Constant(value='%s,%s', kind=None),
                                                            op=Mod(),
                                                            right=Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='ir.ui.view', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='field', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='field', ctx=Store()),
                                                                iter=Name(id='fields', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='query', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='sql', ctx=Load()),
                                                                    attr='SQL',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value="\n                        SELECT {table}.id, {similarity} AS _similarity\n                        FROM {table}\n                        LEFT JOIN ir_ui_view v ON {table}.view_id = v.id\n                        LEFT JOIN ir_translation t ON v.id = t.res_id\n                        WHERE t.lang = {lang}\n                        AND t.name = ANY({names})\n                        AND t.type = 'model_terms'\n                        ORDER BY _similarity desc\n                        LIMIT 1000\n                    ", kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='table',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Identifier',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='model', ctx=Load()),
                                                                            attr='_table',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='similarity',
                                                                value=Name(id='similarity', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='lang',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Placeholder',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='lang', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='names',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Placeholder',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='names', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='similarity', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='sql', ctx=Load()),
                                                                    attr='SQL',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='word_similarity({search}, {field})', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='search',
                                                                value=Call(
                                                                    func=Name(id='unaccent', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='sql', ctx=Load()),
                                                                                attr='Placeholder',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='search', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='field',
                                                                value=Call(
                                                                    func=Name(id='unaccent', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='sql', ctx=Load()),
                                                                                attr='SQL',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='value', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='names', ctx=Store())],
                                                    value=ListComp(
                                                        elt=BinOp(
                                                            left=Constant(value='%s,%s', kind=None),
                                                            op=Mod(),
                                                            right=Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='model', ctx=Load()),
                                                                        attr='_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='field', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='field', ctx=Store()),
                                                                iter=Name(id='fields', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='query', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='sql', ctx=Load()),
                                                                    attr='SQL',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value="\n                        SELECT res_id, {similarity} AS _similarity\n                        FROM ir_translation\n                        WHERE lang = {lang}\n                        AND name = ANY({names})\n                        AND type = 'model'\n                        ORDER BY _similarity desc\n                        LIMIT 1000\n                    ", kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='similarity',
                                                                value=Name(id='similarity', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='lang',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Placeholder',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='lang', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='names',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Placeholder',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='names', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='query', ctx=Load()),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='lang', kind=None),
                                                            Constant(value='names', kind=None),
                                                            Constant(value='search', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='lang',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='names', ctx=Load()),
                                                            Name(id='search', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ids', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='row', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='cr',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='fetchall',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='row', ctx=Load()),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[GtE()],
                                                                        comparators=[Name(id='similarity_threshold', ctx=Load())],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Call(
                                                                func=Name(id='list', ctx=Load()),
                                                                args=[Name(id='ids', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Name(id='AND', ctx=Load()),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='search_read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='domain', ctx=Load()),
                                            Name(id='fields', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Name(id='limit', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='field', ctx=Store()),
                                                    Name(id='value', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='value', ctx=Load()),
                                                            Name(id='str', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='value', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='value', ctx=Load()),
                                                                    attr='lower',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=YieldFrom(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='re', ctx=Load()),
                                                                        attr='findall',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Name(id='match_pattern', ctx=Load()),
                                                                        Name(id='value', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_basic_enumerate_words',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_details', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Browses through all words that need to be compared to the search term.\n        It extracts all words of every field associated to models in the fields_per_model parameter.\n\n        :param search_details: obtained from `_search_get_details()`\n        :param search: search term to which words must be matched against\n        :param limit: maximum number of records fetched per model to build the word list\n        :return: yields words\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='match_pattern', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='\\w{%s,}', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Name(id='min', ctx=Load()),
                                    args=[
                                        Constant(value=4, kind=None),
                                        BinOp(
                                            left=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='search', ctx=Load())],
                                                keywords=[],
                                            ),
                                            op=Sub(),
                                            right=Constant(value=3, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first', ctx=Store())],
                            value=Call(
                                func=Name(id='escape_psql', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='search', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='search_detail', ctx=Store()),
                            iter=Name(id='search_details', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='model_name', ctx=Store()),
                                                Name(id='fields', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Subscript(
                                                value=Name(id='search_detail', ctx=Load()),
                                                slice=Constant(value='model', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='search_detail', ctx=Load()),
                                                slice=Constant(value='search_fields', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='search_detail', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='requires_sudo', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='model', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='model', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='search_detail', ctx=Load()),
                                                slice=Constant(value='base_domain', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fields_domain', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[Name(id='fields', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='intersection',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=Name(id='fields', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fields_domain', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='field', ctx=Load()),
                                                                    Constant(value='=ilike', kind=None),
                                                                    BinOp(
                                                                        left=Constant(value='%s%%', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='first', ctx=Load()),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fields_domain', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='field', ctx=Load()),
                                                                    Constant(value='=ilike', kind=None),
                                                                    BinOp(
                                                                        left=Constant(value='%% %s%%', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='first', ctx=Load()),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fields_domain', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='field', ctx=Load()),
                                                                    Constant(value='=ilike', kind=None),
                                                                    BinOp(
                                                                        left=Constant(value='%%>%s%%', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='first', ctx=Load()),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='OR', ctx=Load()),
                                                args=[Name(id='fields_domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Name(id='AND', ctx=Load()),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='search_read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='domain', ctx=Load()),
                                            Name(id='fields', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1000, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='field', ctx=Store()),
                                                    Name(id='value', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='value', ctx=Load()),
                                                            Name(id='str', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='value', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='value', ctx=Load()),
                                                                    attr='lower',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='field', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='arch_db', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='value', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='text_from_html', ctx=Load()),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        For(
                                                            target=Name(id='word', ctx=Store()),
                                                            iter=Call(
                                                                func=Attribute(
                                                                    value=Name(id='re', ctx=Load()),
                                                                    attr='findall',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='match_pattern', ctx=Load()),
                                                                    Name(id='value', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='word', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Subscript(
                                                                                value=Name(id='search', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Yield(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='word', ctx=Load()),
                                                                                        attr='lower',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
