Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='TransactionCase', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestDisableSnippetsAssets',
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
                                        args=[],
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
                                    attr='View',
                                    ctx=Store(),
                                ),
                            ],
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='WebsiteMenu',
                                    ctx=Store(),
                                ),
                            ],
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='Website',
                                    ctx=Store(),
                                ),
                            ],
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='IrAsset',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.asset', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='homepage',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='View',
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
                                            Constant(value='key', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Home', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Name(id='HOMEPAGE_WITH_OUTDATED_S_WEBSITE_FORM', ctx=Load()),
                                            Constant(value='website.homepage', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mega_menu',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='WebsiteMenu',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='mega_menu_content', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Image Gallery V001', kind=None),
                                            Name(id='MEGA_MENU_CONTENT_IMAGE_GALLERY_V001', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='initial_active_snippets_assets',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_active_snippets_assets',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    name='test_homepage_with_outdated_s_website_form',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Website',
                                        ctx=Load(),
                                    ),
                                    attr='_disable_unused_snippets_assets',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='s_website_form_000', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_snippet_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='s_website_form', kind=None),
                                    Constant(value='000', kind=None),
                                    Constant(value='scss', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='s_website_form_001', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_snippet_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='s_website_form', kind=None),
                                    Constant(value='001', kind=None),
                                    Constant(value='scss', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='s_image_gallery_000', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_snippet_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='s_image_gallery', kind=None),
                                    Constant(value='000', kind=None),
                                    Constant(value='scss', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='s_image_gallery_001', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_snippet_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='s_image_gallery', kind=None),
                                    Constant(value='001', kind=None),
                                    Constant(value='scss', kind=None),
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
                                    Attribute(
                                        value=Name(id='s_website_form_000', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s_website_form_001', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s_image_gallery_000', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s_image_gallery_001', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='unwanted_snippets_assets_changes', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='initial_active_snippets_assets',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    op=Sub(),
                                    right=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_active_snippets_assets',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=Sub(),
                                right=Call(
                                    func=Name(id='set', ctx=Load()),
                                    args=[
                                        List(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='s_image_gallery_000', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
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
                                        args=[Name(id='unwanted_snippets_assets_changes', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    BinOp(
                                        left=Constant(value='Following snippets are not following the snippet versioning system structure, or their previous assets have not been deactivated:\n', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Constant(value='\n', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='unwanted_snippets_assets_changes', ctx=Load())],
                                            keywords=[],
                                        ),
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
                    name='test_homepage_with_s_website_form_V001',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='homepage',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='arch_db', kind=None)],
                                        values=[Name(id='HOMEPAGE_WITH_S_WEBSITE_FORM_V001', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mega_menu',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='mega_menu_content', kind=None)],
                                        values=[Name(id='MEGA_MENU_CONTENT_IMAGE_GALLERY_OUTDATED', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Website',
                                        ctx=Load(),
                                    ),
                                    attr='_disable_unused_snippets_assets',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='s_website_form_000', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_snippet_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='s_website_form', kind=None),
                                    Constant(value='000', kind=None),
                                    Constant(value='scss', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='s_website_form_001', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_snippet_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='s_website_form', kind=None),
                                    Constant(value='001', kind=None),
                                    Constant(value='scss', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='s_image_gallery_000', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_snippet_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='s_image_gallery', kind=None),
                                    Constant(value='000', kind=None),
                                    Constant(value='scss', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='s_image_gallery_001', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_snippet_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='s_image_gallery', kind=None),
                                    Constant(value='001', kind=None),
                                    Constant(value='scss', kind=None),
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
                                    Attribute(
                                        value=Name(id='s_website_form_000', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s_website_form_001', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s_image_gallery_000', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s_image_gallery_001', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
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
                    name='_get_snippet_asset',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='snippet_id', annotation=None, type_comment=None),
                            arg(arg='asset_version', annotation=None, type_comment=None),
                            arg(arg='asset_type', annotation=None, type_comment=None),
                        ],
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='IrAsset',
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
                                                    Constant(value='path', kind=None),
                                                    Constant(value='=', kind=None),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=Constant(value='website/static/src/snippets/', kind=None),
                                                                        op=Add(),
                                                                        right=Name(id='snippet_id', ctx=Load()),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value='/', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Name(id='asset_version', ctx=Load()),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value='.', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='asset_type', ctx=Load()),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_active_snippets_assets',
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
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='IrAsset',
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
                                                            Constant(value='path', kind=None),
                                                            Constant(value='like', kind=None),
                                                            Constant(value='snippets', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='active', kind=None),
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
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='path', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        Assign(
            targets=[Name(id='HOMEPAGE_WITH_S_WEBSITE_FORM_V001', ctx=Store())],
            value=Constant(value='\n<t name="Homepage" t-name="website.homepage1">\n  <t t-call="website.layout">\n    <t t-set="pageName" t-value="\'homepage\'"/>\n    <div id="wrap" class="oe_structure oe_empty">\n      <section class="s_website_form pt16 pb16 o_colored_level" data-vcss="001" data-snippet="s_website_form" data-name="Form">\n        <div class="container">\n          <form action="/website_form/" method="post" enctype="multipart/form-data" class="o_mark_required" data-mark="*" data-success-mode="redirect" data-success-page="/contactus-thank-you" data-model_name="mail.mail">\n          </form>\n        </div>\n      </section>\n      <section class="s_showcase pt48 pb48 o_colored_level" data-vcss="002" data-snippet="s_showcase" data-name="Showcase">\n        <div class="container">\n        </div>\n      </section>\n    </div>\n  </t>\n</t>\n', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='HOMEPAGE_WITH_OUTDATED_S_WEBSITE_FORM', ctx=Store())],
            value=Constant(value='\n<t name="Homepage" t-name="website.homepage1">\n  <t t-call="website.layout">\n    <t t-set="pageName" t-value="\'homepage\'"/>\n    <div id="wrap" class="oe_structure oe_empty">\n      <form action="/website_form/" method="post" class="s_website_form container-fluid mt32 o_fake_not_editable" enctype="multipart/form-data" data-name="Form Builder" data-model_name="mail.mail" data-success_page="/contactus-thank-you" data-snippet="s_website_form">\n        <div class="container">\n        </div>\n      </form>\n      <section class="s_showcase pt48 pb48 o_colored_level" data-vcss="002" data-snippet="s_showcase" data-name="Showcase">\n        <div class="container">\n        </div>\n      </section>\n    </div>\n  </t>\n</t>\n', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='MEGA_MENU_CONTENT_IMAGE_GALLERY_V001', ctx=Store())],
            value=Constant(value='\n<section class="s_mega_menu_multi_menus py-4 o_colored_level" data-name="Multi-Menus">\n        <div class="container">\n        </div>\n    </section>\n\n<section class="s_image_gallery o_slideshow s_image_gallery_show_indicators s_image_gallery_indicators_rounded pt24 o_colored_level" data-vcss="001" data-columns="3" style="height: 500px; overflow: hidden;" data-snippet="s_image_gallery" data-name="Image Gallery">\n        <div class="container">\n        </div>\n    </section>\n', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='MEGA_MENU_CONTENT_IMAGE_GALLERY_OUTDATED', ctx=Store())],
            value=Constant(value='\n<section class="s_mega_menu_multi_menus py-4 o_colored_level" data-name="Multi-Menus">\n        <div class="container">\n        </div>\n    </section>\n\n<section class="s_image_gallery o_slideshow s_image_gallery_show_indicators s_image_gallery_indicators_rounded pt24 o_colored_level" data-columns="3" style="height: 500px; overflow: hidden;" data-snippet="s_image_gallery" data-name="Image Gallery">\n        <div class="container">\n        </div>\n    </section>\n', kind=None),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
