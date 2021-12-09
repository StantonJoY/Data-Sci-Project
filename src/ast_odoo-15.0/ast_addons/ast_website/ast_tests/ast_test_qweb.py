Module(
    body=[
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[alias(name='TransactionCaseWithUserDemo', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.tools',
            names=[alias(name='MockRequest', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_module_resource', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestQweb',
            bases=[Name(id='TransactionCaseWithUserDemo', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_load',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='convert_file',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Constant(value='website', kind=None),
                                    Call(
                                        func=Name(id='get_module_resource', ctx=Load()),
                                        args=[
                                            Name(id='module', ctx=Load()),
                                            Starred(
                                                value=Name(id='args', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
                                    Constant(value='init', kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value='test', kind=None),
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
                    name='test_qweb_post_processing_att',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-escaping">\n                <img src="http://test.external.img/img.png"/>\n                <img t-att-src="url"/>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <img src="http://test.external.img/img.png" loading="lazy"/>\n                <img src="http://test.external.img/img2.png" loading="lazy"/>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
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
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='url', kind=None)],
                                        values=[Constant(value='http://test.external.img/img2.png', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    name='test_qweb_cdn',
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
                                    attr='_load',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website', kind=None),
                                    Constant(value='tests', kind=None),
                                    Constant(value='template_qweb_test.xml', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
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
                                args=[Constant(value='website.default_website', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='cdn_activated', kind=None),
                                            Constant(value='cdn_url', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Constant(value='http://test.cdn', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='demo', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.users', kind=None),
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
                                                        Constant(value='login', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Constant(value='demo', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='demo', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='signature', kind=None)],
                                        values=[Constant(value='<span class="toto">\n                span<span class="fa"></span><img src="/web/image/1"/>\n            </span>', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='demo_env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='user',
                                        value=Name(id='demo', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='demo_env', ctx=Load()),
                                        slice=Constant(value='ir.qweb', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website.test_template', kind=None),
                                    Dict(
                                        keys=[Constant(value='user', kind=None)],
                                        values=[Name(id='demo', ctx=Load())],
                                    ),
                                ],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='asset_data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='etree', ctx=Load()),
                                                attr='HTML',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='html', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='xpath',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='//*[@data-asset-bundle]', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='asset_xmlid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='asset_data', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='data-asset-bundle', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='asset_version', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='asset_data', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='data-asset-version', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\?unique=[^"]+', kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf8', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachments', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='demo_env', ctx=Load()),
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
                                                    Constant(value='url', kind=None),
                                                    Constant(value='=like', kind=None),
                                                    Constant(value='/web/assets/%-%/website.test_bundle.%', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='attachments', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='format_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='js', kind=None),
                                    Constant(value='css', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='filename', kind=None),
                                    Constant(value='alt', kind=None),
                                    Constant(value='asset_xmlid', kind=None),
                                    Constant(value='asset_version', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='attachments', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='url',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='attachments', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='url',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='demo', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Marc%20Demo', kind=None),
                                    Constant(value='Marc Demo', kind=None),
                                    Name(id='asset_xmlid', ctx=Load()),
                                    Name(id='asset_version', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertHTMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='html', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Constant(value='<!DOCTYPE html>\n<html>\n    <head>\n        <link type="text/css" rel="stylesheet" href="http://test.external.link/style1.css"/>\n        <link type="text/css" rel="stylesheet" href="http://test.external.link/style2.css"/>\n        <link type="text/css" rel="stylesheet" href="http://test.cdn%(css)s" data-asset-bundle="%(asset_xmlid)s" data-asset-version="%(asset_version)s"/>\n        <meta/>\n        <script type="text/javascript" src="http://test.external.link/javascript1.js"></script>\n        <script type="text/javascript" src="http://test.external.link/javascript2.js"></script>\n        <script type="text/javascript" src="http://test.cdn%(js)s" data-asset-bundle="%(asset_xmlid)s" data-asset-version="%(asset_version)s"></script>\n    </head>\n    <body>\n        <img src="http://test.external.link/img.png" loading="lazy"/>\n        <img src="http://test.cdn/website/static/img.png" loading="lazy"/>\n        <a href="http://test.external.link/link">x</a>\n        <a href="http://test.cdn/web/content/local_link">x</a>\n        <span style="background-image: url(&#39;http://test.cdn/web/image/2&#39;)">xxx</span>\n        <div widget="html"><span class="toto">\n                span<span class="fa"></span><img src="http://test.cdn/web/image/1" loading="lazy">\n            </span></div>\n        <div widget="image"><img src="http://test.cdn/web/image/res.users/%(user_id)s/avatar_1920/%(filename)s" class="img img-fluid" alt="%(alt)s" loading="lazy"/></div>\n    </body>\n</html>', kind=None),
                                                op=Mod(),
                                                right=Name(id='format_data', ctx=Load()),
                                            ),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf8', kind=None)],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestQwebProcessAtt',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestQwebProcessAtt', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='website',
                                    ctx=Store(),
                                ),
                            ],
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
                                args=[Constant(value='website.default_website', kind=None)],
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
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fr_FR', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='language_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.lang_en', kind=None)],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.lang_fr', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='default_lang_id',
                                    ctx=Store(),
                                ),
                            ],
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
                                args=[Constant(value='base.lang_en', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='cdn_activated',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='cdn_url',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='http://test.cdn', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='cdn_filters',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='\n', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='^(/[a-z]{2}_[A-Z]{2})?/a$', kind=None),
                                            Constant(value='^(/[a-z]{2})?/a$', kind=None),
                                            Constant(value='^/b$', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_test_att',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='expect', annotation=None, type_comment=None),
                            arg(arg='tag', annotation=None, type_comment=None),
                            arg(arg='attribute', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='a', kind=None),
                            Constant(value='href', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
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
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_post_processing_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tag', ctx=Load()),
                                            Dict(
                                                keys=[Name(id='attribute', ctx=Load())],
                                                values=[Name(id='url', ctx=Load())],
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expect', ctx=Load()),
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
                    name='test_process_att_no_request',
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
                                    attr='_test_att',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/', kind=None),
                                    Dict(
                                        keys=[Constant(value='href', kind=None)],
                                        values=[Constant(value='/', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_att',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/en', kind=None),
                                    Dict(
                                        keys=[Constant(value='href', kind=None)],
                                        values=[Constant(value='/en', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_att',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/fr', kind=None),
                                    Dict(
                                        keys=[Constant(value='href', kind=None)],
                                        values=[Constant(value='/fr', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_att',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/a', kind=None),
                                    Dict(
                                        keys=[Constant(value='href', kind=None)],
                                        values=[Constant(value='/a', kind=None)],
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
                    name='test_process_att_no_website',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/en', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/en', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/fr', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/fr', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/a', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/a', kind=None)],
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
                FunctionDef(
                    name='test_process_att_monolang_route',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='website',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='multilang',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/a', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='http://test.cdn/a', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/en/a', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='http://test.cdn/en/a', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/b', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='http://test.cdn/b', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/en/b', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/en/b', kind=None)],
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
                FunctionDef(
                    name='test_process_att_no_request_lang',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='website',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/en/', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/fr/', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/fr', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/fr', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/fr', kind=None)],
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
                FunctionDef(
                    name='test_process_att_with_request_lang',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='website',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='context',
                                                value=Dict(
                                                    keys=[Constant(value='lang', kind=None)],
                                                    values=[Constant(value='fr_FR', kind=None)],
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/fr', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/en/', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/fr/', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/fr', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/fr', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/fr', kind=None)],
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
                FunctionDef(
                    name='test_process_att_matching_cdn_and_lang',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='website',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/a', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='http://test.cdn/a', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/en/a', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='http://test.cdn/a', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/fr/a', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='http://test.cdn/fr/a', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/b', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='http://test.cdn/b', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/en/b', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='http://test.cdn/b', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/fr/b', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/fr/b', kind=None)],
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
                FunctionDef(
                    name='test_process_att_no_route',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='website',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='context',
                                                value=Dict(
                                                    keys=[Constant(value='lang', kind=None)],
                                                    values=[Constant(value='fr_FR', kind=None)],
                                                ),
                                            ),
                                            keyword(
                                                arg='routing',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/web/static/hi', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/web/static/hi', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/my-page', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/fr/my-page', kind=None)],
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
                FunctionDef(
                    name='test_process_att_url_crap',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='website',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='match', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='http', ctx=Load()),
                                                            attr='root',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get_db_router',
                                                        ctx=Load(),
                                                    ),
                                                    attr='return_value',
                                                    ctx=Load(),
                                                ),
                                                attr='bind',
                                                ctx=Load(),
                                            ),
                                            attr='return_value',
                                            ctx=Load(),
                                        ),
                                        attr='match',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/x#y?z', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/x#y?z', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='assert_called_with',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/x', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='method',
                                                value=Constant(value='POST', kind=None),
                                            ),
                                            keyword(
                                                arg='query_args',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='reset_calls',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/x?y#z', kind=None),
                                            Dict(
                                                keys=[Constant(value='href', kind=None)],
                                                values=[Constant(value='/x?y#z', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='assert_called_with',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/x', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='method',
                                                value=Constant(value='POST', kind=None),
                                            ),
                                            keyword(
                                                arg='query_args',
                                                value=Constant(value='y', kind=None),
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
